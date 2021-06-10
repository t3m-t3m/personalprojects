from Condition import Condition
from Rule import Rule


temp_conditions = [
        Condition('холодная', -15, -3, f_type='ldown'),
        Condition('прохладная', -5, 0, 5, 10),
        Condition('теплая', 8, 16, f_type='lup'),
]

hum_conditions = [
        Condition('сухая', 15, 25, f_type='ldown'),
        Condition('нормальная', 20, 32, 50, 75),
        Condition('влажная', 60, 80, f_type='lup'),
]

rules = [
        Rule(temp_conditions[0], hum_conditions[0], 'комфортная холодная'),
        Rule(temp_conditions[0], hum_conditions[1], 'ощутимо холодная'),
        Rule(temp_conditions[0], hum_conditions[2], 'морозная'),
        Rule(temp_conditions[1], hum_conditions[0], 'комфортно прохладная'),
        Rule(temp_conditions[1], hum_conditions[1], 'ощутимо прохладная'),
        Rule(temp_conditions[1], hum_conditions[2], 'промозглая'),
        Rule(temp_conditions[2], hum_conditions[0], 'прохладно-теплая'),
        Rule(temp_conditions[2], hum_conditions[1], 'комфортная'),
        Rule(temp_conditions[2], hum_conditions[2], 'душная'),
]

desc_conditions = [
        Condition('комфортная холодная', 0, 45, f_type='lup'),
        Condition('ощутимо холодная', 0, 20, f_type='lup'),
        Condition('морозная', 0, 70, f_type='lup'),
        Condition('комфортно прохладная', 0, 50, f_type='lup'),
        Condition('ощутимо прохладная', 0, 20, f_type='lup'),
        Condition('промозглая', 0, 20, f_type='lup'),
        Condition('прохладно-теплая', 0, 50, f_type='lup'),
        Condition('комфортная', 0, 40, f_type='lup'),
        Condition('душная', 0, 20, f_type='lup'),
]
