import streamlit as st
import pandas as pd
import math
import requests


st.title("Pokemon Stat Checker")

pokemonOne = st.text_input("Enter the name of a Pokemon.")
pokemonOne = pokemonOne.lower()
url = "https://pokeapi.co/api/v2/pokemon/" + pokemonOne
res = requests.get(url)
if res and pokemonOne:
    st.success("Here are " + pokemonOne.capitalize() +"'s stats")
    isShiny = st.checkbox("Shiny?")
    if isShiny:
        st.image(res.json()['sprites']['front_shiny'], width=200)
    else:
        st.image(res.json()['sprites']['front_default'], width=200)
    st.caption(res.json()["name"].capitalize())
    baseHP = res.json()['stats'][0]['base_stat']
    baseAtt = res.json()['stats'][1]['base_stat']
    baseDef = res.json()['stats'][2]['base_stat']
    baseSpAtt = res.json()['stats'][3]['base_stat']
    baseSpDef = res.json()['stats'][4]['base_stat']
    baseSpd = res.json()['stats'][5]['base_stat']
    baseStats = [baseHP, baseAtt, baseDef, baseSpAtt, baseSpDef, baseSpd]
    chart_data = pd.DataFrame(
        baseStats,
        index=["HP","Att","Def","Sp.Att","Sp.Def","Spd"],
        columns=["Base Stats"]
    )
    st.bar_chart(chart_data)
    abilityNum = st.number_input("Enter a number to learn about one of " + pokemonOne.capitalize() + "'s abilities!", value=0)
    if res.json()['abilities'][abilityNum]:
        abilityUrl = res.json()['abilities'][abilityNum]['ability']['url']
        resTwo = requests.get(abilityUrl)
        if resTwo:
            st.success(resTwo.json()['name'].capitalize() + ":\n\n" + resTwo.json()['effect_entries'][1]['effect'])
        else:
            st.error("Out of range, try a smaller number!")
    perfIVs = st.radio("Do you want perfect IVs?", options=["Yes","No"])
    if perfIVs == "Yes":
        hpIVs = 31
        attIVs = 31
        defIVs = 31
        spattIVs = 31
        spdefIVs = 31
        spdIVs = 31
    elif perfIVs == "No":
        hpIVs = st.slider("How many IVs will your HP stat have?", value = 0, step = 1, max_value=31, min_value=0)
        attIVs = st.slider("How many IVs will your Att stat have?", value=0, step=1, max_value=31, min_value=0)
        defIVs = st.slider("How many IVs will your Def stat have?", value=0, step=1, max_value=31, min_value=0)
        spattIVs = st.slider("How many IVs will your Sp.Att stat have?", value=0, step=1, max_value=31, min_value=0)
        spdefIVs = st.slider("How many IVs will your Sp.Def stat have?", value=0, step=1, max_value=31, min_value=0)
        spdIVs = st.slider("How many IVs will your Spd stat have?", value=0, step=1, max_value=31, min_value=0)

    hpEVs = st.slider("How many EVs will your HP stat have?", value=0, step=1, max_value=252, min_value=0)
    attEVs = st.slider("How many EVs will your Att stat have?", value=0, step=1, max_value=252, min_value=0)
    defEVs = st.slider("How many EVs will your Def stat have?", value=0, step=1, max_value=252, min_value=0)
    spattEVs = st.slider("How many EVs will your Sp.Att stat have?", value=0, step=1, max_value=252, min_value=0)
    spdefEVs = st.slider("How many EVs will your Sp.Def stat have?", value=0, step=1, max_value=252, min_value=0)
    spdEVs = st.slider("How many EVs will your Spd stat have?", value=0, step=1, max_value=252, min_value=0)

    if hpEVs + attEVs + defEVs + spattEVs + spdefEVs + spdEVs > 510:
        st.error("Illegal EV total. Total EVs cannot exceed 510.")
        hpEVs = 0
        attEVs = 0
        defEVs = 0
        spattEVs = 0
        spdefEVs = 0
        spdEVs = 0

    attMult = 1
    defMult = 1
    spattMult = 1
    spdefMult = 1
    spdMult = 1

    nature = st.selectbox("Select your nature",
                          options=["Hardy","Lonely","Adamant","Naughty","Brave",
                                   "Bold","Docile","Impish","Lax","Relaxed",
                                   "Modest","Mild","Bashful","Rash","Quiet",
                                   "Calm","Gentle","Careful","Quirky","Sassy",
                                   "Timid","Hasty","Jolly","Naive","Serious"])
    if nature == "Lonely":
        attMult = 1.1
        defMult = 0.9
    elif nature == "Adamant":
        attMult = 1.1
        spattMult = 0.9
    elif nature == "Naughty":
        attMult = 1.1
        spdefMult = 0.9
    elif nature == "Brave":
        attMult = 1.1
        spdMult = 0.9
    elif nature == "Bold":
        defMult = 1.1
        attMult = 0.9
    elif nature == "Impish":
        defMult = 1.1
        spattMult = 0.9
    elif nature == "Lax":
        defMult = 1.1
        spdefMult = 0.9
    elif nature == "Relaxed":
        defMult = 1.1
        spdMult = 0.9
    elif nature == "Modest":
        spattMult = 1.1
        attMult = 0.9
    elif nature == "Mild":
        spattMult = 1.1
        defMult = 0.9
    elif nature == "Rash":
        spattMult = 1.1
        spdefMult = 0.9
    elif nature == "Quiet":
        spattMult = 1.1
        spdMult = 0.9
    elif nature == "Calm":
        spdefMult = 1.1
        attMult = 0.9
    elif nature == "Gentle":
        spdefMult = 1.1
        defMult = 0.9
    elif nature == "Careful":
        spdefMult = 1.1
        spattMult = 0.9
    elif nature == "Sassy":
        spdefMult = 1.1
        spdMult = 0.9
    elif nature == "Timid":
        spdMult = 1.1
        attMult = 0.9
    elif nature == "Hasty":
        spdMult = 1.1
        defMult = 0.9
    elif nature == "Jolly":
        spdMult = 1.1
        spattMult = 0.9
    elif nature == "Naive":
        spdMult = 1.1
        spdefMult = 0.9

    HP = math.floor((int((2*baseHP + hpIVs + int(hpEVs / 4))) * 100) / 100) + 110
    Att = int(int((int((2*baseAtt + attIVs + int(attEVs / 4)) * 100) / 100) + 5)*attMult)
    Def = int(int((int((2*baseDef + defIVs + int(defEVs / 4)) * 100) / 100) + 5)*defMult)
    SpAtt = int(int((int((2*baseSpAtt + spattIVs + int(spattEVs / 4)) * 100) / 100) + 5)*spattMult)
    SpDef = int(int((int((2*baseSpDef + spdefIVs + int(spdefEVs / 4)) * 100) / 100) + 5)*spdefMult)
    Spd = int(int((int((2*baseSpd + spdIVs + int(spdEVs / 4)) * 100) / 100) + 5)*spdMult)

    stats = [HP, Att, Def, SpAtt, SpDef, Spd]
    total_stats = pd.DataFrame(
        stats,
        index=["HP", "Att", "Def", "Sp.Att", "Sp.Def", "Spd"],
        columns=["Total Stats"]
    )
    st.dataframe(total_stats)
else:
    st.error("Pokemon not found!")

with st.sidebar:
    st.write("Welcome to the Pokemon Stat Checker")

if st.button("Press to play music"):
    st.audio('Media/pokemusic.mp3')


