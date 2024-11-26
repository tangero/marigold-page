---
layout: post
title: "Rate-Splitting Multiple Access (RSMA)"
date: 2024-11-25
categories: [LTE, 4G, Mobilní sítě]
---

### Princip fungování RSMA

Rate-Splitting Multiple Access (RSMA) představuje inovativní přístupovou techniku pro bezdrátové komunikační systémy, která kombinuje výhody tradičních ortogonálních přístupových metod a non-ortogonálních přístupů jako je NOMA. Základním principem RSMA je rozdělení uživatelských dat na společnou část a soukromou část, což přináší větší flexibilitu při správě interference mezi uživateli.

V RSMA vysílač rozdělí zprávu každého uživatele na dvě části - společnou a soukromou. Společné části zpráv od všech uživatelů jsou sloučeny do jednoho datového proudu, který je zakódován způsobem umožňujícím jeho dekódování všemi příjemci. Soukromé části zpráv jsou zpracovány samostatně a jsou určeny pouze pro konkrétní uživatele. Vysílač poté použije předkódování (precoding) k vytvoření vysílacího signálu, který obsahuje jak společnou, tak soukromé části.

Na přijímací straně uživatelé nejprve dekódují společnou část zprávy pomocí techniky postupného rušení interference (SIC). Po úspěšném dekódování a odstranění společné části ze přijatého signálu může každý uživatel dekódovat svou soukromou část zprávy. Tento hierarchický přístup k dekódování umožňuje efektivnější správu interference mezi uživateli a poskytuje robustnější výkon v podmínkách s nepřesnou znalostí stavu kanálu.

![Rate-Splitting Multiple Access (RSMA)](/assets/RSMA.jpg)

**Výběr soukromé a společné části zprávy v RSMA** je komplexní optimalizační problém, který závisí na několika klíčových faktorech. Vysílač musí zvolit optimální rozdělení na základě aktuálních podmínek kanálu, požadavků na kvalitu služby a interference mezi uživateli.

Proces rozdělení zprávy začíná analýzou kanálových podmínek mezi vysílačem a všemi přijímači. Vysílač bere v úvahu kvalitu kanálu každého uživatele (SNR - Signal-to-Noise Ratio), vzájemnou interferenci mezi uživateli a také míru neurčitosti v odhadu kanálu (Channel State Information - CSI). Čím větší je nejistota v CSI, tím větší část dat je typicky přidělena do společné části, protože ta je robustnější vůči chybám v odhadu kanálu.

Pro matematickou optimalizaci rozdělení se používá maximalizace vážené sumy dosažitelných přenosových rychlostí (weighted sum-rate) s ohledem na omezení celkového vysílacího výkonu. 

Tato optimalizace zahrnuje několik proměnných:
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

**👉 Přehled nových přístupů k multiplexování:** \
- [Non-Orthogonal Multiple Access (NOMA)](/mobilnisite/Non-Orthogonal-Multiple-Access-NOMA/)
- [Rate-Splitting Multiple Access (RSMA)](/mobilnisite/Rate-Splitting-Multiple-Access-RSMA/)
- [Sparse Code Multiple Access (SCMA)](/mobilnisite/Sparse-Code-Multiple-Access-SCMA/)
- další [experimentální přístupy k multiplexování](/mobilnisite/pokrocile-multiplexovani/)
- a pro pořádek povídání o tom, [jak funguje OFDMA](/mobilnisite/ofdma)