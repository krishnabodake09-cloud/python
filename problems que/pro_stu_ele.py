m=65
att=80
m_ok=m>=50
a_ok=att>=75
eligibal=m_ok and a_ok
one_condition= m_ok or a_ok
not_eligibal= 'not eligible'
print('AND= ' ,eligibal)
print('or= ', one_condition)
print('not= ', not_eligibal)