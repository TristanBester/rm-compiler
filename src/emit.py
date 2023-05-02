class Emitter:
    def __init__(self):
        self.propositions = []
        self.language = ""

    def declare_proposition(self, name):
        self.propositions.append(name)

    def init_assignments(self):
        # Initialise truth table
        self.assignments = []

        for i in range(2 ** len(self.propositions)):
            assignment = []

            for j in range(1, len(self.propositions) + 1):
                assignment.append(not ((i % 2**j) < (2 ** (j - 1))))
            self.assignments.append(assignment)

    def _get_prop_idx(self, prop_name):
        for i, x in enumerate(self.propositions):
            if x == prop_name:
                return i
        return None

    def _get_satisfying_assignment_idx(self, prop, truth_value):
        prop_idx = self._get_prop_idx(prop)

        satisfying_assignment_idx = []

        for i, a in enumerate(self.assignments):
            if a[prop_idx] == truth_value:
                satisfying_assignment_idx.append(i)
        return satisfying_assignment_idx

    def block_while(self, proposition, truth_value):
        print(proposition, truth_value, self._get_prop_idx(proposition))

        satisfying_assignment_idx = self._get_satisfying_assignment_idx(
            proposition, truth_value
        )
        other_assignments_idx = self._get_satisfying_assignment_idx(
            proposition, not truth_value
        )

        self.language += "("

        for i in satisfying_assignment_idx:
            self.language += str(i) + " + "

        self.language = self.language[:-3] + ")*"

        self.language += "("

        for i in other_assignments_idx:
            self.language += str(i) + " + "

        self.language = self.language[:-3] + ")"
