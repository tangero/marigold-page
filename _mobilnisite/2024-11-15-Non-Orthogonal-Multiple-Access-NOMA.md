---
layout: post
title: "Non-Orthogonal Multiple Access (NOMA)"
date: 2024-11-25
categories: [LTE, 4G, Mobilní sítě]
---

Orthogonal Frequency Division Multiple Access (OFDMA) se stal základem pro technologie 4G LTE a 5G NR díky své schopnosti efektivně rozdělit dostupné frekvenční spektrum mezi uživatele. Přestože OFDMA nabízí vysokou spektrální efektivitu a robustnost vůči interferenci, vývoj směrem k sítím 6G s sebou přináší potřebu alternativ, které by mohly zlepšit využití spektra, podporovat masivní konektivitu a umožnit přenosy dat s nízkou latencí. Mezi nejvýznamnější technologie, které se zvažují jako doplňky nebo náhrady OFDMA, patří Non-Orthogonal Multiple Access (NOMA), Rate-Splitting Multiple Access (RSMA) a Sparse Code Multiple Access (SCMA). Pojďme si tyto přístupy projít... 

## Non-Orthogonal Multiple Access (NOMA)

### Princip fungování NOMA

NOMA opouští klíčovou vlastnost OFDMA – ortogonálnost kanálů – a umožňuje více uživatelům sdílet stejnou frekvenční podnož. Rozdíl spočívá v tom, že uživatelé jsou rozlišováni na základě úrovní výkonu nebo jiných parametrů, což umožňuje simultánní přenos více datových toků. 

Základním principem NOMA je současné vysílání signálů od různých uživatelů na stejné frekvenci, přičemž se tyto signály liší v úrovni vysílacího výkonu. Základnová stanice strategicky přiděluje různé úrovně výkonu jednotlivým uživatelům podle jejich podmínek kanálu. Typicky uživatelé s horšími podmínkami kanálu, například ti, kteří jsou více vzdálení nebo mají v cestě více překážek, dostávají přidělený vyšší vysílací výkon. Naopak uživatelé s lepšími podmínkami kanálu vysílají s nižším výkonem.

Pro rozlišení těchto překrývajících se signálů se na přijímací straně využívá sofistikovaná technika nazvaná **Successive Interference Cancellation (SIC)**. Tento proces funguje postupně - nejprve dekóduje nejsilnější signál z přijatého složeného signálu. Po úspěšném dekódování je tento silný signál odečten od původního přijatého signálu, což umožní dekódovat další, slabší signál. Tento proces se opakuje, dokud nejsou dekódovány všechny překryté signály.

![Non-Orthogonal Multiple Access (NOMA)](/assets/OFDMA-II-NON-ORTHOGONAL-MULTIPLE-ACCESS-NOMA.png)

Díky tomuto přístupu NOMA dosahuje výrazně vyšší spektrální účinnosti než tradiční přístupové metody. Umožňuje obsloužit více uživatelů současně a snižuje latenci komunikace. Zároveň však klade vyšší nároky na implementaci, především v oblasti SIC dekódování a přesného řízení výkonu. Přijímače musí být výpočetně výkonnější, aby zvládly složitější zpracování signálu. I přes tyto výzvy představuje NOMA významný krok vpřed v oblasti přístupových metod a je považována za klíčovou technologii pro zvyšování kapacity budoucích mobilních sítí.

Tato technika je obzvláště účinná v situacích, kdy síť musí obsloužit velké množství uživatelů s různými kvalitami signálu, což je typický scénář v hustě obydlených městských oblastech. NOMA tak přispívá k efektivnějšímu využití omezeného rádiového spektra a pomáhá uspokojit rostoucí poptávku po mobilních datových službách.

### Výhody NOMA proti OFDMA

1.	Vyšší spektrální efektivita: Díky simultánnímu sdílení kanálů je možné zvýšit počet uživatelů na jednotku spektra.
2.	Podpora masivní konektivity: Ideální pro IoT aplikace, kde je potřeba připojit velké množství zařízení s nízkými nároky na přenosovou rychlost.
3.	Flexibilita: NOMA umožňuje efektivněji využít rozdíly v kanálových podmínkách mezi uživateli.

### Uplatnění a vývoj NOMA

Technologie NOMA byla intenzivně zkoumána v rámci výzkumných projektů pro 5G a je považována za klíčovou složku pro 6G sítě. Společnosti jako Huawei a ZTE aktivně podporují její zahrnutí do standardů 3GPP. Huawei představil variantu Power-Domain NOMA, která využívá rozdíly ve výkonu signálů, zatímco další varianty, jako Code-Domain NOMA, zkoumají využití specifických kódovacích schémat.