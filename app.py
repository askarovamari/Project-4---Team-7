import flask
import pandas as pd
from joblib import dump, load


with open(f'baseball_stats.joblib', 'rb') as f:
    model = load(f)


app = flask.Flask(__name__, template_folder='template')


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return (flask.render_template('web.html'))

    if flask.request.method == 'POST':
        exit_velocity_avg = flask.request.form['exit_velocity_avg']
        launch_angle_avg = flask.request.form['launch_angle_avg']
        sweet_spot_percent = flask.request.form['sweet_spot_percent']
        barrel_batted_rate = flask.request.form['barrel_batted_rate']
        solidcontact_percent = flask.request.form['solidcontact_percent']
        flareburner_percent = flask.request.form['flareburner_percent']
        poorlyunder_percent = flask.request.form['poorlyunder_percent']
        poorlytopped_percent = flask.request.form['poorlytopped_percent']
        poorlyweak_percent = flask.request.form['poorlyweak_percent']
        hard_hit_percent = flask.request.form['hard_hit_percent']
        avg_best_speed = flask.request.form['avg_best_speed']
        avg_hyper_speed = flask.request.form['avg_hyper_speed']
        z_swing_percent = flask.request.form['z_swing_percent']
        z_swing_miss_percent = flask.request.form['z_swing_miss_percent']
        oz_swing_percent = flask.request.form['oz_swing_percent']
        oz_swing_miss_percent = flask.request.form['oz_swing_miss_percent']
        oz_contact_percent = flask.request.form['oz_contact_percent']
        meatball_swing_percent = flask.request.form['meatball_swing_percent']
        iz_contact_percent = flask.request.form['iz_contact_percent']
        whiff_percent = flask.request.form['whiff_percent']
        swing_percent = flask.request.form['swing_percent']
        pull_percent = flask.request.form['pull_percent']
        straightaway_percent = flask.request.form['straightaway_percent']
        opposite_percent = flask.request.form['opposite_percent']
        f_strike_percent = flask.request.form['f_strike_percent']
        groundballs_percent = flask.request.form['groundballs_percent']
        flyballs_percent = flask.request.form['flyballs_percent']
        linedrives_percent = flask.request.form['linedrives_percent']
        popups_percent = flask.request.form['popups_percent']

        input_variables = pd.DataFrame([[exit_velocity_avg, launch_angle_avg, sweet_spot_percent,
                                         barrel_batted_rate, solidcontact_percent, flareburner_percent,
                                         poorlyunder_percent, poorlytopped_percent, poorlyweak_percent, hard_hit_percent,
                                         avg_best_speed, avg_hyper_speed, z_swing_percent, z_swing_miss_percent,
                                         oz_swing_percent, oz_swing_miss_percent, oz_contact_percent, meatball_swing_percent,
                                         iz_contact_percent, whiff_percent, swing_percent, pull_percent, straightaway_percent,
                                         opposite_percent, f_strike_percent, groundballs_percent, flyballs_percent,
                                         linedrives_percent, popups_percent]],
                                       columns=['exit_velocity_avg', 'launch_angle_avg', 'sweet_spot_percent',
                                         'barrel_batted_rate', 'solidcontact_percent', 'flareburner_percent',
                                         'poorlyunder_percent', 'poorlytopped_percent', 'poorlyweak_percent', 'hard_hit_percent',
                                         'avg_best_speed', 'avg_hyper_speed', 'z_swing_percent', 'z_swing_miss_percent',
                                         'oz_swing_percent', 'oz_swing_miss_percent', 'oz_contact_percent', 'meatball_swing_percent',
                                         'iz_contact_percent', 'whiff_percent', 'swing_percent', 'pull_percent', 'straightaway_percent',
                                         'opposite_percent', 'f_strike_percent', 'groundballs_percent', 'flyballs_percent',
                                         'linedrives_percent', 'popups_percent'],
                                       dtype='float',
                                       index=['input'])

        predictions = model.predict(input_variables)
        print(predictions)

        return flask.render_template('web.html', original_input={'exit_velocity_avg':exit_velocity_avg, 'launch_angle_avg':launch_angle_avg, 'sweet_spot_percent':sweet_spot_percent,
                                         'barrel_batted_rate':barrel_batted_rate, 'solidcontact_percent':solidcontact_percent, 'flareburner_percent':flareburner_percent,
                                         'poorlyunder_percent':poorlyunder_percent, 'poorlytopped_percent':poorlytopped_percent, 'poorlyweak_percent':poorlyweak_percent, 'hard_hit_percent':hard_hit_percent,
                                         'avg_best_speed':avg_best_speed, 'avg_hyper_speed':avg_hyper_speed, 'z_swing_percent':z_swing_percent, 'z_swing_miss_percent':z_swing_miss_percent,
                                         'oz_swing_percent':oz_swing_percent, 'oz_swing_miss_percent':oz_swing_miss_percent, 'oz_contact_percent':oz_contact_percent, 'meatball_swing_percent':meatball_swing_percent,
                                         'iz_contact_percent':iz_contact_percent, 'whiff_percent':whiff_percent, 'swing_percent':swing_percent, 'pull_percent':pull_percent, 'straightaway_percent':straightaway_percent,
                                         'opposite_percent':opposite_percent, 'f_strike_percent':f_strike_percent, 'groundballs_percent':groundballs_percent, 'flyballs_percent':flyballs_percent,
                                         'linedrives_percent':linedrives_percent, 'popups_percent':popups_percent},
                                     result=predictions)


if __name__ == '__main__':
    app.run(debug=True)
