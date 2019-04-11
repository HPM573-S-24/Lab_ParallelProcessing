from ParallelClasses import ParallelMultiCohort
import ProbilisticParamClasses as P
import InputData as D
import MultiCohortSupport as Support
import SimPy.SamplePathClasses as Path
import SimPy.FigureSupport as Fig

N_COHORTS = 100              # number of cohorts
therapy = P.Therapies.MONO  # selected therapy


if __name__ == '__main__':  # this line is needed to avoid errors that occur on Windows computers

    # create multiple cohort
    multiCohort = ParallelMultiCohort(
        ids=range(N_COHORTS),
        pop_size=D.POP_SIZE,
        therapy=therapy)

    multiCohort.simulate(sim_length=D.SIM_LENGTH)

    # plot the sample paths
    Path.graph_sample_paths(
        sample_paths=multiCohort.multiCohortOutcomes.survivalCurves,
        title='Survival Curves',
        x_label='Time-Step (Year)',
        y_label='Number Survived',
        transparency=0.5)

    # plot the histogram of average survival time
    Fig.graph_histogram(
        data=multiCohort.multiCohortOutcomes.meanSurvivalTimes,
        title='Histogram of Mean Survival Time',
        x_label='Mean Survival Time (Year)',
        y_label='Count')

    # print the outcomes of this simulated cohort
    Support.print_outcomes(multi_cohort_outcomes=multiCohort.multiCohortOutcomes,
                           therapy_name=therapy)
