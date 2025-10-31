from hypothesis import strategies as st

from dataratz.domain.child import Child

child_strategy = st.builds(
    Child,
    id=st.uuids(),
    first_name=st.text(min_size=3, max_size=20),
    last_name=st.integers(min_value=3, max_value=20),
)