---
layout: post
title: "Sparse Code Multiple Access (SCMA)"
date: 2024-11-25
categories: [LTE, 4G, Mobilní sítě]
hide: true
---

### Princip fungování SCMA

Základním principem SCMA (Sparse Code Multiple Access) je přímé mapování bitů každého uživatele na speciálně navržená řídká krycí hesla, která jsou uložena v přiděleném kódovníku.

V praxi to funguje tak, že každému uživateli je přidělen unikátní kódovník obsahující sadu řídkých vícerozměrných krycích hesel. Pojem "řídká" zde znamená, že většina prvků v každém krycím hesle je nulová, což je klíčové pro efektivní zpracování signálu. Když uživatel potřebuje přenést data, jeho vstupní bity jsou přímo mapovány na odpovídající krycí hesla z jeho kódovníku. Toto přímé mapování je efektivnější než tradiční dvoustupňový proces používaný například v CDMA, kde se nejprve provádí modulace a poté rozprostření signálu.

![Sparse Code Multiple Access (SCMA)](/assets/SCMA.png)

SCMA záměrně umožňuje, aby se signály od různých uživatelů částečně překrývaly ve stejných rádiových zdrojích. Díky řídké struktuře krycích hesel dochází k překryvu pouze v některých dimenzích, což je zásadní pro následnou detekci na přijímači. Tento přístup umožňuje systému obsloužit více uživatelů, než je počet dostupných rádiových zdrojů, což vede k vyšší spektrální účinnosti.

Na přijímací straně se používá sofistikovaný iterativní algoritmus nazývaný Message Passing Algorithm (MPA). Tento algoritmus využívá řídkou strukturu krycích hesel k efektivnímu oddělení překrývajících se signálů. MPA pracuje na principu postupné výměny pravděpodobnostních informací mezi uzly reprezentujícími uživatele a uzly reprezentujícími rádiové zdroje. V každé iteraci se zpřesňuje odhad přenášených dat, dokud není dosaženo dostatečné přesnosti.

Ukažme si to na příkladu vícenásobného přístupu 6 uživatelů s kódovými knihami specifickými pro vrstvu SCMA.
Každému uživateli je přidělena jedna kódová kniha SCMA (v uvedeném příkladu si uživatel i vezme kódovou knihu pro vrstvu i, i = 1, 2, ..., 6). Po použití kodéru FEC jsou pak kódované bity každého uživatele namapovány na kódové slovo SCMA podle jemu přiřazeného kódového svazku. Kódová slova SCMA se dále kombinují nad tóny OFDM a symboly se přenášejí v podobě bloků SCMA, podobně jako v případě koncepce bloků zdrojů v LTE.


![Vícenásobný přístup pomocí Sparse Code Multiple Access (SCMA)](/assets/Multiple-Access-with-SCMA.png)


Klíčovým faktorem pro výkon SCMA je návrh kódovníků. Ty musí být pečlivě optimalizovány tak, aby:
- Minimalizovaly vzájemnou interferenci mezi uživateli
- Maximalizovaly Euklidovskou vzdálenost mezi jednotlivými krycími hesly v rámci každého kódovníku
- Zachovávaly vhodnou míru řídkosti pro efektivní dekódování
- Poskytovaly dobré vlastnosti pro tvarování konstelace signálu

SCMA přináší několik významných výhod oproti tradičním přístupovým metodám:
- Umožňuje vyšší spektrální účinnost díky možnosti obsloužit více uživatelů na stejných rádiových zdrojích
- Poskytuje nižší latenci díky současnému přístupu více uživatelů
- Nabízí dobrý výkon i při vysokém zatížení sítě
- Vykazuje zvýšenou odolnost vůči rušení díky sofistikovanému kódování a detekci

Tato technologie představuje významný krok vpřed v oblasti vícenásobného přístupu a je považována za klíčovou součást budoucích mobilních sítí, zejména v kontextu masivního připojení IoT zařízení a scénářů s vysokou hustotou uživatelů.

### Výhody SCMA proti OFDMA

1.	Zlepšená energetická efektivita: Sparsní kódování minimalizuje spotřebu energie při přenosu.
2.	Podpora masivního připojení: SCMA je vhodné pro sítě IoT a další aplikace, kde je potřeba připojit velký počet zařízení.
3.	Nižší latence: Díky optimalizovanému kódování může SCMA dosáhnout rychlejšího přenosu dat.

### Uplatnění a vývoj SCMA

SCMA bylo poprvé navrženo ve výzkumu pro 5G, ale jeho plný potenciál by mohl být využit až v 6G sítích. Technologie je podporována společnostmi jako NTT DOCOMO, které zkoumají její aplikaci ve scénářích zahrnujících IoT a komunikaci mezi vozidly. SCMA se také jeví jako vhodná technologie pro spektrální sdílení mezi více operátory.

![Uplatnění Sparse Code Multiple Access (SCMA)](/assets/SCMA-Application-Scenarios.png)


**👉 Přehled nových přístupů k multiplexování:** \
- [Non-Orthogonal Multiple Access (NOMA)](/mobilnisite/Non-Orthogonal-Multiple-Access-NOMA/)
- [Rate-Splitting Multiple Access (RSMA)](/mobilnisite/Rate-Splitting-Multiple-Access-RSMA/)
- [Sparse Code Multiple Access (SCMA)](/mobilnisite/Sparse-Code-Multiple-Access-SCMA/)
- další [experimentální přístupy k multiplexování](/mobilnisite/pokrocile-multiplexovani/)
- a pro pořádek povídání o tom, [jak funguje OFDMA](/mobilnisite/ofdma)