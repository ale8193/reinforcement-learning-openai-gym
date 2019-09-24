import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from collections import namedtuple

EpisodeStats = namedtuple("Stats", ["episode_lengths", "episode_rewards"])


def plot_episode_stats(stats, smoothing_window=10, noshow=False, goal_value=None, fig_size=(15, 8)):
    # Plot the episode length over time
    fig1 = plt.figure(figsize=fig_size)
    plt.plot(stats.episode_lengths)
    plt.xlabel("Episode")
    plt.ylabel("Episode Length")
    plt.title("Episode Length over Time")
    if noshow:
        plt.close(fig1)
    else:
        plt.show(fig1)

    # Plot the episode reward over time
    fig2 = plt.figure(figsize=fig_size)
    rewards_smoothed = pd.Series(stats.episode_rewards).rolling(smoothing_window, min_periods=smoothing_window).mean()
    plt.plot(rewards_smoothed)
    plt.xlabel("Episode")
    plt.ylabel("Episode Reward (Smoothed)")
    title = "Episode Reward over Time (Smoothed over window size {})".format(smoothing_window)

    if goal_value is not None:
        plt.axhline(goal_value, color='g', linestyle='dashed')
        title = "Episode Reward over Time (Smoothed over window size" \
                " " + str(smoothing_window) + ", goal value " + str(goal_value) + ")"

    plt.title(title)
    if noshow:
        plt.close(fig2)
    else:
        plt.show(fig2)

    # Plot time steps and episode number
    fig3 = plt.figure(figsize=fig_size)
    plt.plot(np.cumsum(stats.episode_lengths), np.arange(len(stats.episode_lengths)))
    plt.xlabel("Time Steps")
    plt.ylabel("Episode")
    plt.title("Episode per time step")
    if noshow:
        plt.close(fig3)
    else:
        plt.show(fig3)

    return fig1, fig2, fig3