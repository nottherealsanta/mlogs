import numpy as np
from optuna.study import StudyDirection
# import matplotlib.image as mpimg
# from IPython.display import HTML
# import matplotlib.animation as animation
from pathlib import Path
import matplotlib.pyplot as plt
import optuna

script_path = Path(__file__).parent.absolute()

_min = 0
_max = 1


def g(x):
    return x * np.cos((np.array(3.6 * np.pi)) * x)


def custom_callback_1d(study, trial):

    df = study.trials_dataframe()
    if study.direction == StudyDirection.MINIMIZE:
        def flag(x):
            return True if x == df.value.min() else False
        df["best"] = df.value.apply(flag)

    elif study.direction == StudyDirection.MAXIMIZE:
        def flag(x):
            return True if x == df.value.max() else False
        df["best"] = df.value.apply(flag)
    else:
        return 0

    X = np.arange(_min, _max, 0.01)
    plt.plot(X, [g(x) for x in X])
    plt.scatter(df.params_x, df.value)
    plt.scatter(df[df.best].params_x, df[df.best].value, marker="*", s=250, alpha=0.5)
    plt.scatter(df.tail(1).params_x, df.tail(1).value, marker="+", s=150)

    plt.savefig(f"{script_path}/assets/{df.shape[0]}.png")
    plt.show()


def objective(trial):
    x = trial.suggest_uniform("x", _min, _max)
    return g(x)


study = optuna.create_study(
    study_name="g_of_x",
    direction="minimize",
)
study.optimize(objective, n_trials=20, callbacks=[custom_callback_1d])

import imageio
images = []
for filename in range(20):
    images.append(imageio.imread(f"{script_path}/assets/{filename+1}.png"))

imageio.mimsave(f"{script_path}/assets/optuna_animation.gif", images)