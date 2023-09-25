import streamlit as st
import random 

if 'random_text' not in st.session_state:
    st.session_state.random_text = ''

if 'random_emoji_dict' not in st.session_state:
    st.session_state.random_emoji_dict = {}

if 'selected_emoji' not in st.session_state:
    st.session_state.selected_emoji = ''

if 'vRefresh' not in st.session_state:
    st.session_state.vRefresh = True

if 'disableButton' not in st.session_state:
    st.session_state.disableButton = False


vocab = {
    'DOG': '🐶',
    'PIG':'🐷',
    'HEN':'🐔',
    'MONKEY': '🐵',
    'FOX':'🦊',
    'ZEBRA':'🦓',
    'COW':'🐄',
    'RABBIT':'🐰',
    'UNICORN':'🦄',
    'CAMEL':'🐪',
    'ELEPHANT':'🐘',
    'MOUSE':'🐭',
    'SNAKE':'🐍'
}


def get_random_text(vocab):
    key_list = list(vocab.keys())
    return random.choice(key_list)

def get_random_emojis(vocab):
    random_text = get_random_text(vocab)
    key_list = list(vocab.keys())
    key_list[0] = random_text
    key_list = key_list[:5]
    random.shuffle(key_list)
    random_emoji_dict = {k:vocab[k] for k in key_list}
    return random_text, random_emoji_dict

if st.session_state.vRefresh:
    st.session_state.random_text, st.session_state.random_emoji_dict = get_random_emojis(vocab)

st.header(f':blue[{st.session_state.random_text}]')
    


col1, col2, col3, col4 = st.columns(4)

cols = [col1, col2, col3, col4]



recol1, _,_,_ = st.columns(4)
with recol1:
    if st.button('🔃',use_container_width=True):
        st.session_state.vRefresh = False
        st.session_state.selected_emoji = ''
        st.session_state.disableButton = False
        st.experimental_rerun()

# if st.session_state.selected_emoji == st.session_state.random_text:
#     st.session_state.disableButton = True
#     st.balloons()
#     st.success('✔')
#     st.session_state.vRefresh = True
# else:
#     st.session_state.vRefresh = False
#     if st.session_state.selected_emoji != '':
#         st.error(f'❌ {st.session_state.selected_emoji}')
 
for col, (k,v) in zip(cols, st.session_state.random_emoji_dict.items()):
    with col:
        if st.button(v,key =v, use_container_width=True):
            st.session_state.selected_emoji = k


if st.session_state.selected_emoji == st.session_state.random_text:
    st.session_state.disableButton = True
    # st.experimental_rerun()
    st.balloons()
    st.success('✔')
    st.session_state.vRefresh = True
else:
    st.session_state.vRefresh = False
    if st.session_state.selected_emoji != '':
        st.error(f'❌ {st.session_state.selected_emoji}')




# st.info(f"st.session_state.random_text : {st.session_state.random_text}")
# st.info(f"st.session_state.random_emoji_dict : {st.session_state.random_emoji_dict}")
# st.info(f"st.session_state.selected_emoji : {st.session_state.selected_emoji}")
# st.info(f"st.session_state.vRefresh : {st.session_state.vRefresh}")
# st.info(f"st.session_state.disableButton : {st.session_state.disableButton}")
