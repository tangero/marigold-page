---
layout: post
title: "Budoucnost frekvenčního multiplexu: Alternativy k OFDMA a jejich role v 6G"
date: 2024-11-25
categories: [LTE, 4G, Mobilní sítě]
---

Budoucnost frekvenčního multiplexu: Alternativy k OFDMA a jejich role v 6G

Orthogonal Frequency Division Multiple Access (OFDMA) se stal základem pro technologie 4G LTE a 5G NR díky své schopnosti efektivně rozdělit dostupné frekvenční spektrum mezi uživatele. Přestože OFDMA nabízí vysokou spektrální efektivitu a robustnost vůči interferenci, vývoj směrem k sítím 6G s sebou přináší potřebu alternativ, které by mohly zlepšit využití spektra, podporovat masivní konektivitu a umožnit přenosy dat s nízkou latencí. Mezi nejvýznamnější technologie, které se zvažují jako doplňky nebo náhrady OFDMA, patří Non-Orthogonal Multiple Access (NOMA), Rate-Splitting Multiple Access (RSMA) a Sparse Code Multiple Access (SCMA).

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

## Rate-Splitting Multiple Access (RSMA)

### Princip fungování RSMA

Rate-Splitting Multiple Access (RSMA) představuje inovativní přístupovou techniku pro bezdrátové komunikační systémy, která kombinuje výhody tradičních ortogonálních přístupových metod a non-ortogonálních přístupů jako je NOMA. Základním principem RSMA je rozdělení uživatelských dat na společnou část a soukromou část, což přináší větší flexibilitu při správě interference mezi uživateli.

V RSMA vysílač rozdělí zprávu každého uživatele na dvě části - společnou a soukromou. Společné části zpráv od všech uživatelů jsou sloučeny do jednoho datového proudu, který je zakódován způsobem umožňujícím jeho dekódování všemi příjemci. Soukromé části zpráv jsou zpracovány samostatně a jsou určeny pouze pro konkrétní uživatele. Vysílač poté použije předkódování (precoding) k vytvoření vysílacího signálu, který obsahuje jak společnou, tak soukromé části.

Na přijímací straně uživatelé nejprve dekódují společnou část zprávy pomocí techniky postupného rušení interference (SIC). Po úspěšném dekódování a odstranění společné části ze přijatého signálu může každý uživatel dekódovat svou soukromou část zprávy. Tento hierarchický přístup k dekódování umožňuje efektivnější správu interference mezi uživateli a poskytuje robustnější výkon v podmínkách s nepřesnou znalostí stavu kanálu.

**Výběr soukromé a společné části zprávy v RSMA** je komplexní optimalizační problém, který závisí na několika klíčových faktorech. Vysílač musí zvolit optimální rozdělení na základě aktuálních podmínek kanálu, požadavků na kvalitu služby a interference mezi uživateli.

Proces rozdělení zprávy začíná analýzou kanálových podmínek mezi vysílačem a všemi přijímači. Vysílač bere v úvahu kvalitu kanálu každého uživatele (SNR - Signal-to-Noise Ratio), vzájemnou interferenci mezi uživateli a také míru neurčitosti v odhadu kanálu (Channel State Information - CSI). Čím větší je nejistota v CSI, tím větší část dat je typicky přidělena do společné části, protože ta je robustnější vůči chybám v odhadu kanálu.

Pro matematickou optimalizaci rozdělení se používá maximalizace vážené sumy dosažitelných přenosových rychlostí (weighted sum-rate) s ohledem na omezení celkového vysílacího výkonu. Tato optimalizace zahrnuje několik proměnných:
- poměr rozdělení dat mezi společnou a soukromou část pro každého uživatele
- alokace vysílacího výkonu pro společnou a soukromé části
- návrh předkódovacích vektorů pro obě části

Prakticky se často používají sub-optimální algoritmy, které nabízejí dobrý kompromis mezi výpočetní složitostí a výkonem. Tyto algoritmy mohou být založeny například na gradientních metodách nebo na heuristických přístupech využívajících předchozí zkušenosti s podobnými kanálovými podmínkami.

U uživatelů s podobnými kanálovými podmínkami se větší část jejich dat typicky přiděluje do společné části, zatímco u uživatelů s výrazně odlišnými podmínkami se více dat přenáší v soukromých částech. To umožňuje efektivnější správu interference a lepší využití dostupných rádiových zdrojů.

RSMA nabízí několik významných výhod oproti konvenčním přístupům. Je více odolná vůči nepřesnostem v odhadu kanálu než NOMA a poskytuje lepší spektrální účinnost než ortogonální metody. Díky flexibilnímu rozdělení dat mezi společnou a soukromou část může systém dynamicky přizpůsobovat poměr rozdělení podle aktuálních podmínek kanálu a požadavků na kvalitu služby. Tato adaptabilita činí RSMA vhodnou pro různorodé scénáře nasazení, od masivních MIMO systémů až po multicastové přenosy.

Implementace RSMA však vyžaduje sofistikovanější zpracování signálu na vysílací i přijímací straně ve srovnání s tradičními přístupovými metodami. Je třeba řešit optimální rozdělení dat mezi společnou a soukromou část, návrh předkódovacích matic a efektivní alokaci výkonu. Přesto se RSMA jeví jako slibná technologie pro budoucí bezdrátové systémy, zejména v kontextu heterogenních sítí a scénářů s různorodými požadavky na služby.

### Výhody RSMA proti OFDMA

1.	Robustnost vůči interferenci: RSMA využívá precizní řízení rozkladu toku a koordinaci mezi uživateli, čímž minimalizuje interferenci.
2.	Univerzálnost: Lze ji aplikovat na různá spektra a scénáře – od nízké hustoty uživatelů po masivní připojení.
3.	Optimalizace výkonu: Zlepšuje efektivitu při přenosu dat mezi uživateli s velmi odlišnými podmínkami kanálu.

### Uplatnění a vývoj RSMA

RSMA je propagována jako technologie, která by mohla překlenout nedostatky NOMA v případech, kdy je potřeba větší řízení přenosu. Ericsson a Qualcomm jsou mezi společnostmi, které se podílejí na výzkumu a standardizaci RSMA v rámci 3GPP. Technologie již byla otestována v akademických i průmyslových scénářích a ukazuje slibné výsledky v oblastech, jako je sdílení spektra mezi mobilními a satelitními sítěmi.

## Sparse Code Multiple Access (SCMA)

### Princip fungování SCMA

Základním principem SCMA (Sparse Code Multiple Access) je přímé mapování bitů každého uživatele na speciálně navržená řídká krycí hesla, která jsou uložena v přiděleném kódovníku.

V praxi to funguje tak, že každému uživateli je přidělen unikátní kódovník obsahující sadu řídkých vícerozměrných krycích hesel. Pojem "řídká" zde znamená, že většina prvků v každém krycím hesle je nulová, což je klíčové pro efektivní zpracování signálu. Když uživatel potřebuje přenést data, jeho vstupní bity jsou přímo mapovány na odpovídající krycí hesla z jeho kódovníku. Toto přímé mapování je efektivnější než tradiční dvoustupňový proces používaný například v CDMA, kde se nejprve provádí modulace a poté rozprostření signálu.

SCMA záměrně umožňuje, aby se signály od různých uživatelů částečně překrývaly ve stejných rádiových zdrojích. Díky řídké struktuře krycích hesel dochází k překryvu pouze v některých dimenzích, což je zásadní pro následnou detekci na přijímači. Tento přístup umožňuje systému obsloužit více uživatelů, než je počet dostupných rádiových zdrojů, což vede k vyšší spektrální účinnosti.

Na přijímací straně se používá sofistikovaný iterativní algoritmus nazývaný Message Passing Algorithm (MPA). Tento algoritmus využívá řídkou strukturu krycích hesel k efektivnímu oddělení překrývajících se signálů. MPA pracuje na principu postupné výměny pravděpodobnostních informací mezi uzly reprezentujícími uživatele a uzly reprezentujícími rádiové zdroje. V každé iteraci se zpřesňuje odhad přenášených dat, dokud není dosaženo dostatečné přesnosti.

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

SCMA bylo poprvé navrženo ve výzkumu pro 5G, ale jeho plný potenciál by mohl být využit až v 6G sítích. Technologie je podporována společnostmi jako NTT DOCOMO, které zkoumají její aplikaci ve scénářích zahrnujících IoT a vehikulární komunikaci. SCMA se také jeví jako vhodná technologie pro spektrální sdílení mezi více operátory.

## Porovnání technologií: Jak si vedou proti OFDMA?

| Technologie |	Hlavní výhody |	Případné nevýhody |	Podporující společnosti |
| NOMA |	Vyšší spektrální efektivita, podpora IoT |	Vyšší složitost SIC	Huawei, ZTE |
| RSMA |	Robustnost vůči interferenci, univerzálnost	| Náročné řízení přenosu |	Ericsson, Qualcomm |
| SCMA |	Energetická efektivita, podpora IoT |	Vyšší složitost kódování |	NTT DOCOMO |

## Budoucnost a výhled pro 6G

Sítě 6G přinesou zcela nové výzvy v oblasti řízení spektra, včetně podpory extrémně vysokých přenosových rychlostí, masivní konektivity a ultra-nízké latence. Technologie jako NOMA, RSMA a SCMA nabízejí slibné alternativy nebo doplňky k OFDMA, avšak každá z nich má své specifické výhody a omezení. V budoucnosti se pravděpodobně dočkáme kombinace těchto technologií, která zajistí optimální využití spektra pro různé aplikace.

Existují ale i další přístupy, které zatím existují jen v konceptech, kdy se zkoumá několik nových přístupů k multiplexování. Zde jsou hlavní směry výzkumu, které si zmiňujeme pro úplnost:

** Spatial Scattering Modulation (SSM)**:
- Využívá prostorové rozptylové charakteristiky kanálu
- Umožňuje přenos dodatečných informací pomocí výběru vzorců rozptylu
- Vhodné zejména pro systémy s masivním MIMO
- Potenciálně energeticky účinnější než tradiční prostorové multiplexování

**Index Modulation (IM)**:
- Přenáší dodatečné informace pomocí aktivace/deaktivace různých přenosových prvků
- Může být aplikováno na různé domény (frekvence, prostor, čas)
- Nabízí dobrý kompromis mezi spektrální a energetickou účinností
- Nižší implementační složitost ve srovnání s některými jinými pokročilými technikami

**Orbital Angular Momentum (OAM) Multiplexing**:
- Využívá orbitální moment hybnosti elektromagnetických vln
- Umožňuje vytvoření několika ortogonálních kanálů v prostoru
- Potenciálně velmi vysoká spektrální účinnost
- Zatím ve fázi základního výzkumu, čelí výzvám v praktické implementaci

**Reconfigurable Intelligent Surface (RIS) Assisted Multiple Access**:
- Využívá inteligentní odrazné plochy pro optimalizaci přenosových cest
- Umožňuje aktivní tvarování rádiového prostředí
- Může významně zlepšit pokrytí a kapacitu systému
- Kombinovatelné s jinými přístupovými technikami

Tyto techniky jsou zatím ve fázi výzkumu a vývoje. Očekává se, že budoucí sítě 6G budou pravděpodobně využívat kombinaci několika těchto přístupů v závislosti na konkrétních požadavcích aplikací a podmínkách prostředí.

Klíčovou otázkou zůstává standardizace těchto technologií v rámci 3GPP. Zatímco společnosti jako Huawei, Ericsson nebo Qualcomm hrají v tomto procesu hlavní roli, bude důležité, aby se zapojili i další hráči a akademické instituce. Sítě 6G nebudou pouze o rychlejších datech, ale také o efektivnějším a udržitelnějším využití spektra – což je cíl, k němuž tyto technologie směřují.