import agate

#tester = agate.TypeTester(force={'通道': agate.Boolean()})强制指定类型
purchases = agate.Table.from_csv('data.csv', encoding='GBK')
print(purchases)
#agate.Table.print_structure(purchases)     #两种查看列名和数据类型
print(purchases.columns['通道'])
exonerations = agate.Table.from_csv('20.csv', row_names=lambda r: '%(电池名)s' % (r))   #添加列名

print(exonerations.rows[0])
print(exonerations.rows['M45182110100D3'])
for row in exonerations.rows[:5]:
    print(row['电池名'])
median = exonerations.aggregate(agate.Median('通道'))
print(median)
with_age = exonerations.where(lambda row: row['通道'] is not None)    #where方法按照lambda 函数筛选出符合条件的所有行，组成新的Table
for row in exonerations.rows[:5]:
    print(row[:])
print(len(exonerations.rows) - len(with_age.rows))
with_years_in_prison = exonerations.compute([
    ('years_in_prison', agate.Change('convicted', 'exonerated'))
])

with_years_in_prison.aggregate(agate.Median('years_in_prison'))
#print(with_age)
#by_county = purchases.group_by('电池名')

'''totals = by_county.aggregate([
    ('county_cost', agate.Sum('total_cost'))
])

totals = totals.order_by('county_cost', reverse=True)
totals.limit(10).print_bars('county', 'county_cost', width=80)'''