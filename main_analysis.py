"""
This is an integrated script to output different visualization figures and output data in .mat format,
after running the run.py.
Different modules can also run separately.
"""

from plot_pitch_prediction_comparison import make_comparison_figure_from_history_folder
from plot_surprise_with_pianoroll import make_pianoroll_surprise_figure_from_history_folder
from outputs_in_mat_format import export_mat_from_history_folder


if __name__ == '__main__':
    selected_experiment_history_folder = 'experiment_history/03-06-21_12.14.35/' # change your desired 'selected_experiment_history_folder' here!

    print('Making comparison figures:')
    make_comparison_figure_from_history_folder(selected_experiment_history_folder)
    print('Making pianoroll and surprise figures:')
    make_pianoroll_surprise_figure_from_history_folder(selected_experiment_history_folder)
    print('Exporting mat files:')
    export_mat_from_history_folder(selected_experiment_history_folder)