import os
import json


# Your jitendex folder after extracting from zip
# ex:  C:\\Users\\<YOURNAME>\\Downloads\jitendex
yomitan_path = "C:\\Users\\cartr\\Downloads\kanjidic_experiment\\jitendex-yomitan_test"
dir = os.listdir(yomitan_path)
final_list = []
arbitrary_boolean = False
for file in dir:
    if file.startswith("term_bank"):
        arbitrary_boolean = True
        print(F"Loading term bank from {file}")
        term_bank_path = os.path.join(yomitan_path,file)
        with open(term_bank_path, encoding='utf-8')  as f:
            # weakness:when a kana entry has two different kanjis ex: ノリ has both id entries for 海苔 and 乗り, in this case,  the first one is linked
            term_bank_data_raw =f.read() 
            parsed_json = json.loads(term_bank_data_raw)


            for entry in parsed_json:
                # some entries with redirections are negatives(ex:  つまらねー is　-1008190 TH)
                entry_id = abs(entry[6])
                id_data = {"value":entry_id,"displayValue":f"{entry_id}"}
                new_entry = [entry[0], "freq",id_data]


                final_list.append(new_entry)

                print(f"{entry[0]} : {entry_id}")
print(f"Number of entry saved: {len(final_list)}")

if(arbitrary_boolean):
    with open('term_meta_bank_1.json', 'w', encoding="utf-8")  as f:
        json.dump(final_list, f, ensure_ascii=False)
else:
    print("No term banks found")




