pip install streamlit

# main.py
import streamlit as st


def main():
    # Title
    st.title('Meal Planner')
    # Header
    st.header('Header')
    # Text
    st.text('Some text')
    # SubHeader
    st.subheader('Sub header')
    # MarkDownText
    st.markdown('**Markdown is available **')
    # LaTeX Text
    st.latex(r'\bar{X} = \frac{1}{N} \sum_{n=1}^{N} x_i')
    # Code
    st.code('print(\'Hello, World!\')')
    # ErrorMessage
    st.error('Error message')
    # WarningMessage
    st.warning('Warning message')
    # InformationMessage
    st.info('Information message')
    # SuccessMessage
    st.success('Success message')
    # Exception
    st.exception(Exception('Oops!'))
    # Dictionary
    d = {
        'foo': 'bar',
        'users': [
            'alice',
            'bob',
        ],
    }
    st.json(d)

if __name__ == "__main__":
    main()

streamlit run main.py
