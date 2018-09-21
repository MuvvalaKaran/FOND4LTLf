from dfagame.PDDLparser.formula import FormulaOneOf, FormulaAnd
import copy

class Domain:

    def __init__(self, name, requirements, types, constants, predicates, operators):
        self.name = name #string
        self.requirements = requirements #list
        self.types = types #list
        self.constants = constants #list
        self.predicates = predicates #list
        self.operators = operators #list

    def __str__(self):
        if ':non-deterministic' in self.requirements:
            self.requirements.remove(':non-deterministic')
        domain_str = '(define (domain {0})\n'.format(self.name)
        domain_str += '\t(:requirements {0})\n'.format(' '.join(self.requirements))
        if self.types:
            domain_str += '\t(:types {0})\n'.format(' '.join(self.types))
        if self.constants:
            domain_str += '\t(:constants {0})\n'.format(' '.join(map(str, self.constants)))
        domain_str += '\t(:predicates {0})\n'.format(' '.join(map(str, self.predicates)))

        for op in self.operators:
            domain_str += '\t(:action {0})\n'.format(str(op).replace('\n', '\n\t'))

        domain_str += ')'
        return domain_str

    def add_operator_trans(self, transition_operator):
        self.operators.append(transition_operator)

    def add_predicates(self, fluents, states):
        self.predicates.append('(turnDomain)')
        for state in states:
            self.predicates.append('(q{0})'.format(str(state)))
        for fluent in fluents:
            self.predicates.append('({0})'.format(fluent))

    def add_constants(self, states):
        for state in states:
            self.constants.append('{0}'.format(str(state)))

    def add_precond_effect(self):
        for op in self.operators:
            if isinstance(op, str):
                pass
            else:
                if op.isOneOf():
                    oneof_fluent = str(op.effects)
                    self.predicates.append(oneof_fluent)
                else:
                    pass
            op.add_turn_domain()

    def get_new_domain(self, fluents, states, transition_operator):
        #self.add_constants(states)
        self.add_predicates(fluents, states)
        self.add_precond_effect()
        self.add_operator_trans(transition_operator)
        return self

    def get_oneofs(self):
        oneofs = []
        for operator in self.operators:
            if isinstance(operator.effects, FormulaOneOf):
                oneofs.append(operator.effects)
        return oneofs

    def delete_oneofs_placeholder(self):
        temp = copy.deepcopy(self.predicates)
        for predicate in temp:
            if predicate._name.startswith('ONEOF'):
                if predicate in self.predicates:
                    self.predicates.remove(predicate)
            else:
                pass

    def replace_oneofs(self, oneof_list):
        for operator in self.operators:
            if isinstance(operator.effects, FormulaAnd):
                for predicate in operator.effects.andList:
                    if predicate.predicate.name.startswith('ONEOF'):
                        # print(operator.effects.andList.index(predicate))
                        oneof_item = predicate.predicate.name.split('-')
                        id = oneof_item[1]
                        variables_ = oneof_item[2:]
                        new_formula = change_oneof(id, variables_, oneof_list)
                        operator.effects.andList[operator.effects.andList.index(predicate)] = new_formula
            else:
                pass
        return self

def change_oneof(id, _variables, original_oneof_list):
    for oneof_formula in original_oneof_list:
        if oneof_formula.id == id:
            # substitute variables inside oneof items
            legend = dict(zip(oneof_formula.variables_order, _variables))
            new = substitute_variables(oneof_formula, legend)
            # oneof_formula.flag = False
            # print(oneof_formula)
            return new

def substitute_variables(formula, legend):
    # print(legend)
    subformulas_list = []
    for subformula in formula.oneofList:
        temp = copy.deepcopy(subformula)
        for item in temp.andList:
            grounded_var = ''
            for arg in item.predicate._args:
                grounded_var += '-'+str(legend[arg])
            item.predicate._name = item.predicate._name.upper()+grounded_var
            # print(item.predicate._name)
            item.predicate._args = []
        subformula = copy.deepcopy(temp)
        subformulas_list.append(subformula)
    return FormulaOneOf('new', subformulas_list, False)