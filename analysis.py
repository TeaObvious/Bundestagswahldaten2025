from pandas_ods_reader import read_ods

path = "wahldaten.ods"

old_states = ["Nordrhein-Westfalen",
              "Bayern",
              "Baden-Württemberg",
              "Niedersachsen",
              "Hessen",
              "Rheinland-Pfalz",
              "Schleswig-Holstein",
              "Berlin",
              "Saarland",
              "Hamburg",
              "Bremen"]

new_states = ["Sachsen",
              "Brandenburg",
              "Thüringen",
              "Sachsen-Anhalt",
              "Mecklenburg-Vorpommern"]

final_result_absolute = {}
summe = [0, 0]

for state in old_states + new_states:
    df = read_ods(path, state)
    data = {}
    for partydata in df.values:
        party = partydata[0]
        result = [partydata[1], partydata[4]]

        if party == 'CSU' or party == 'CDU':
            party = 'Union'

        if party == 'GRÜNE/B 90':
            party = 'GRÜNE'

        if party not in final_result_absolute:
            try:
                print("adding %s" % party)
                final_result_absolute[party] = [0, 0]
            except Exception as e:
                print(party, e)
        if isinstance(result[0], float) or isinstance(result[0], int):
            final_result_absolute[party][0] += result[0]
            summe[0] += result[0]
        if isinstance(result[1], float) or isinstance(result[1], int):
            final_result_absolute[party][1] += result[1]
            summe[1] += result[1]

final_result_percent = {}
for party, result in final_result_absolute.items():
    final_result_percent[party] = [result[0] / summe[0] * 100, result[1] / summe[1] * 100]

data = {k: v for k, v in sorted(final_result_percent.items(), key=lambda item: -item[1][0]) if v[0] > 5 or v[1] > 5}
print(data)
