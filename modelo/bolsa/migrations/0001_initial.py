# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-03-18 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustoBovespa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('termo_opcoes', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Taxa de termo/opções')),
                ('ana', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Taxa de ANA')),
                ('emolumentos', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Emolumentos')),
            ],
            options={
                'verbose_name': 'Custo Bovespa/Soma',
                'verbose_name_plural': 'Custos Bovespa/Soma',
            },
        ),
        migrations.CreateModel(
            name='CustoCblc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_liquido', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Valor líquido das operações')),
                ('taxa_liquidacao', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Taxa de liquidação')),
                ('taxa_registro', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Taxa de registro')),
                ('operacao', models.CharField(choices=[('C', 'COMPRA'), ('V', 'VENDA'), ('D', 'DIVIDENDOS'), ('S', 'SPLIT')], max_length=100, verbose_name='Operação')),
            ],
            options={
                'verbose_name': 'Custo CBLC',
                'verbose_name_plural': 'Custos CBLC',
            },
        ),
        migrations.CreateModel(
            name='CustoCorretagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corretagem', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Corretagem')),
                ('iss_pis_cofins', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='ISS / PIS / COFINS')),
                ('irrf_operacoes', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='I.R.R.F. s/ operações. Base R$ 0,00')),
                ('outras_bovespa', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Outras Bovespa')),
            ],
            options={
                'verbose_name': 'Corretagem / Despesa',
                'verbose_name_plural': 'Corretagem / Despesas',
            },
        ),
        migrations.CreateModel(
            name='Lancamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data')),
                ('papel', models.CharField(choices=[('ABEV3', 'AMBEV S/A'), ('BBAS3', 'BRASIL'), ('BBDC3', 'BRADESCO'), ('BBDC4', 'BRADESCO'), ('BBSE3', 'BBSEGURIDADE'), ('BRAP4', 'BRADESPAR'), ('BRFS3', 'BRF SA'), ('BRKM5', 'BRASKEM'), ('BRML3', 'BR MALLS PAR'), ('BVMF3', 'BMFBOVESPA'), ('CCRO3', 'CCR SA'), ('CIEL3', 'CIELO'), ('CMIG4', 'CEMIG'), ('CSAN3', 'COSAN'), ('CSNA3', 'SID NACIONAL'), ('ECOR3', 'ECORODOVIAS'), ('ELET3', 'ELETROBRAS'), ('EMBR3', 'EMBRAER'), ('EQTL3', 'EQUATORIAL'), ('ESTC3', 'ESTACIO PART'), ('FIBR3', 'FIBRIA'), ('GGBR4', 'GERDAU'), ('GOAU4', 'GERDAU MET'), ('HYPE3', 'HYPERMARCAS'), ('ITSA4', 'ITAUSA'), ('ITUB4', 'ITAUUNIBANCO'), ('JBSS3', 'JBS'), ('KLBN11', 'KLABIN S/A'), ('KROT3', 'KROTON'), ('LAME4', 'LOJAS AMERIC'), ('LREN3', 'LOJAS RENNER'), ('MRVE3', 'MRV'), ('MULT3', 'MULTIPLAN'), ('NATU3', 'NATURA'), ('PCAR4', 'P.ACUCAR-CBD'), ('PETR3', 'PETROBRAS'), ('PETR4', 'PETROBRAS'), ('QUAL3', 'QUALICORP'), ('RADL3', 'RAIADROGASIL'), ('RAIL3', 'RUMO S.A.'), ('RENT3', 'LOCALIZA'), ('SANB11', 'SANTANDER BR'), ('SBSP3', 'SABESP'), ('SUZB5', 'SUZANO PAPEL'), ('TAEE11', 'TAESA'), ('UGPA3', 'ULTRAPAR'), ('USIM5', 'USIMINAS'), ('VALE3', 'VALE'), ('VIVT4', 'TELEF BRASIL'), ('WEGE3', 'WEG')], max_length=100, verbose_name='Papel')),
                ('operacao', models.CharField(choices=[('C', 'COMPRA'), ('V', 'VENDA'), ('D', 'DIVIDENDOS'), ('S', 'SPLIT')], max_length=100, verbose_name='Operação')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
            ],
            options={
                'verbose_name': 'lançamento',
                'verbose_name_plural': 'lançamentos',
            },
        ),
        migrations.CreateModel(
            name='PlanoDeContas',
            fields=[
                ('classification', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Classificação')),
                ('new_classification', models.CharField(max_length=100, verbose_name='Nova Classificação')),
                ('name', models.CharField(max_length=100, verbose_name='Descrição')),
                ('reduced_account', models.CharField(max_length=100, verbose_name='Conta reduzida')),
                ('sn', models.CharField(max_length=100, verbose_name='SN')),
                ('n', models.CharField(max_length=5, verbose_name='N')),
                ('source', models.CharField(max_length=100, verbose_name='Origem')),
                ('account_type', models.CharField(max_length=100, verbose_name='Tipo Conta')),
            ],
        ),
        migrations.AddField(
            model_name='custocorretagem',
            name='lancamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custo_corretagem', to='bolsa.Lancamento'),
        ),
        migrations.AddField(
            model_name='custocblc',
            name='lancamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custo_cblc', to='bolsa.Lancamento'),
        ),
        migrations.AddField(
            model_name='custobovespa',
            name='lancamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custo_bovespa', to='bolsa.Lancamento'),
        ),
    ]
