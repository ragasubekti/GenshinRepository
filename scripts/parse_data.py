import json

def get_audio(game_data, version, is_diff = False):
    temp_audio = ""

    for lang in game_data['voice_packs']:

        gaver = game_data['version']
        glang = lang['language']
        gpath = lang['path']

        if is_diff is False:
            temp_audio += f"[Audio {glang} {version}]({gpath})\n"
        else:
            temp_audio += f"[Audio {glang} from {gaver} to {version}]({gpath})\n"

    
    return temp_audio

with open("./genshin.json", "r") as genshin_raw:
    genshin_data = json.load(genshin_raw)
    genshin_data = genshin_data['data']['game']

    temp_file = open("temp.txt", "w+")

    latest_version = genshin_data['latest']
    diffs = genshin_data['diffs']

    temp_text = ""

    temp_text += f"[Game Data {latest_version['version']}]({latest_version['path']})"
    temp_text += get_audio(latest_version, latest_version['version'], False)


    for diff in diffs:
        temp_text += f"[Game Data from {diff['version']} to {latest_version['version']}]({diff['path']})"
        temp_text += get_audio(diff, latest_version['version'], True)
        

    temp_file.write(temp_text)
    temp_file.close()

    
