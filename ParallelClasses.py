import multiprocessing as mp

from ProbabilisticClasses import MultiCohort

MAX_PROCESSES = mp.cpu_count()  # maximum number of processors


def simulate_this_cohort(cohort, sim_length):
    """
    :param cohort: a cohort of patients
    :param sim_length: simulation length
    :return: cohort after being simulated
    """

    # simulate and return the cohort
    cohort.simulate(sim_length)
    return cohort


class ParallelMultiCohort(MultiCohort):

    def __init__(self, ids, pop_size, therapy):
        """
        :param ids: (list) of ids for cohorts to simulate
        :param pop_size: (int) population size of cohorts to simulate
        :param therapy: selected therapy
        """

        MultiCohort.__init__(self, ids, pop_size, therapy)

        # make cohorts
        self.cohorts = []


    def simulate(self, sim_length, n_processes=MAX_PROCESSES):

        # create a list of arguments for simulating the cohorts in parallel

        # simulate all cohorts in parallel

        # outcomes from simulating all cohorts
        for cohort in simulated_cohorts:
            self.multiCohortOutcomes.extract_outcomes(cohort)

        # calculate the summary statistics of from all cohorts
        self.multiCohortOutcomes.calculate_summary_stats()
