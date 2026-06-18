---
slug: "afs"
url: "/mobilnisite/slovnik/afs/"
type: "slovnik"
title: "AFS – Adaptive Multi-Rate Full Rate Speech"
date: 2025-01-01
abbr: "AFS"
fullName: "Adaptive Multi-Rate Full Rate Speech"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/afs/"
summary: "AFS je režim hlasového kodeku v rámci rodiny Adaptive Multi-Rate (AMR), který pracuje na plnorychlostním kanálu (22,8 kbit/s) v sítích GSM/EDGE. Dynamicky přizpůsobuje svou přenosovou rychlost a ochra"
---

AFS je režim plnorychlostního hlasového kodeku v rodině AMR pro sítě GSM/EDGE, který dynamicky přizpůsobuje svou přenosovou rychlost a ochranu proti chybám na základě rádiových podmínek, aby optimalizoval kvalitu hlasu a kapacitu sítě.

## Popis

AFS (Adaptive Multi-Rate Full Rate Speech) je specifický provozní režim adaptivního hlasového kodeku Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)), standardizovaného organizací 3GPP pro systémy GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)). Funguje na plnorychlostním provozním kanálu ([TCH/F](/mobilnisite/slovnik/tch-f/)) s hrubou přenosovou rychlostí 22,8 kbit/s. Základním principem AFS je jeho adaptivní povaha: nepracuje na jedné pevné přenosové rychlosti. Místo toho vybírá z osmi režimů zdrojového kodeku v rozsahu od 4,75 kbit/s do 12,2 kbit/s (včetně režimu kodeku [ETSI](/mobilnisite/slovnik/etsi/) GSM Enhanced Full Rate). Zbývající kapacita kanálu po alokaci bitů pro hlasovou datovou část je využita pro korekci chyb ([FEC](/mobilnisite/slovnik/fec/)) prostřednictvím kanálového kódování. Síť, konkrétně řadič základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)), dynamicky volí optimální režim kodeku na základě měření kvality rádiového kanálu v reálném čase, jako je síla signálu a míra chybovosti bitů.

Z architektonického hlediska implementace AFS zahrnuje jak mobilní stanici ([MS](/mobilnisite/slovnik/ms/)), tak síťové prvky. Kódování hlasu probíhá v MS a v převodníkové jednotce (TCU), která je často umístěna v řadiči základnových stanic (BSC) nebo v mediální bráně (MGW). BSC hraje klíčovou roli, protože přijímá hlášení o měřeních od MS a od základnové stanice (BTS) o aktuální kvalitě rádiového spoje. Na základě těchto informací BSC provádí algoritmus adaptace režimu AMR, aby rozhodl, zda nařídit změnu na jiný režim kodeku – například přechod z režimu s vysokou přenosovou rychlostí (jako 12,2 kbit/s) nabízejícího nejlepší kvalitu hlasu na robustnější režim s nižší přenosovou rychlostí (jako 4,75 kbit/s) se silnější FEC při zvýšeném rušení. Tento příkaz je odeslán pomocí vnitropásmového signalizování uvnitř hlasového rámce.

Úlohou AFS v síti je maximalizovat spektrální účinnost a zvýšit robustnost kvality hlasu. Tím, že umožňuje výměnu přenosové rychlosti hlasového kodeku za zvýšenou ochranu proti chybám, poskytuje AFS významné zvýšení tolerance vůči chybám kanálu ve srovnání se staršími kodeky s pevnou rychlostí, jako je GSM Full Rate (FR) nebo Enhanced Full Rate (EFR). To přímo vede ke zlepšené kvalitě hlasu na okrajích buňky nebo v oblastech se špatným pokrytím a může zvýšit kapacitu sítě tím, že umožní přijatelné kvality hovorů při nižších poměrech nosná/rušení (C/I). Adaptace je typicky pomalá, v řádu sekund, aby odpovídala relativně pomalým charakteristikám útlumu rádiového kanálu a aby se zabránilo nadměrnému přepínání režimů. AFS je klíčovou součástí celkové funkčnosti kodeku AMR, která zahrnuje také režim Adaptive Multi-Rate Half Rate Speech (AHS) pro provoz na polorychlostních kanálech, což poskytuje další zisky v kapacitě.

## K čemu slouží

AFS byl vytvořen, aby řešil omezení hlasových kodeků s pevnou rychlostí v sítích GSM, především kompromis mezi kvalitou hlasu a odolností proti chybám. Předchozí kodeky před AMR, jako GSM Full Rate (FR) a Enhanced Full Rate (EFR), používaly statické přidělování bitů pro hlas a kanálové kódování. Za dobrých rádiových podmínek to bylo neefektivní, protože nadbytečné bity pro kanálové kódování byly promrhány, zatímco za špatných podmínek byla pevná úroveň ochrany často nedostatečná, což vedlo k výraznému zhoršení hlasu nebo přerušeným hovorům. Průmysl potřeboval inteligentnější kodek, který by mohl tento kompromis dynamicky optimalizovat.

Motivace pro AFS a širší kodek AMR byla hnací silou potřeby zlepšit kvalitu hlasových služeb a zvýšit kapacitu sítě bez nutnosti nového spektra nebo dalších lokalit buněk. Zavedením adaptability mohl stejný fyzický rádiový kanál podporovat vyšší kvalitu hlasu, když byly podmínky dobré, a robustnější, byť mírně nižší kvalitu hlasu, když se podmínky zhoršily. Tato adaptabilita přímo řešila problém nekonzistentní kvality hlasu, kterou zažívali mobilní uživatelé, zejména v náročných rádiových prostředích. Umožnila operátorům zlepšit spokojenost zákazníků a potenciálně zpřísnit vzory opakování kmitočtů, čímž zvýšila počet současných hovorů, které síť mohla zvládnout.

Historicky byl AFS součástí zavedení kodeku AMR ve 3GPP Release 4 (ačkoli je často spojován s pozdějšími releasy pro specifické funkce), což představovalo významný vývoj od kodeku GSM EFR. Poskytl zpětně kompatibilní cestu upgradu pro stávající sítě GSM, protože struktura plnorychlostního kanálu zůstala nezměněna; pouze interpretace bitového toku byla adaptována. To učinilo nasazení AFS pro operátory relativně přímočarým, což jim umožnilo získat výhody adaptivního hlasového kódování na jejich stávající infrastruktuře a otevřelo cestu k efektivnějšímu využití cenného rádiového spektra vyhrazeného pro hlasové služby.

## Klíčové vlastnosti

- Dynamický výběr režimu kodeku z osmi přenosových rychlostí (4,75; 5,15; 5,90; 6,70; 7,40; -7,95; 10,2; 12,2 kbit/s)
- Pracuje na plnorychlostním provozním kanálu GSM (TCH/F) s rychlostí 22,8 kbit/s
- Adaptace spoje řízená BSC na základě měření kvality rádiového signálu
- Vnitropásmová signalizace pro příkazy a indikace režimu kodeku
- Vylepšená odolnost proti chybám prostřednictvím adaptivní alokace kanálového kódování
- Zpětná kompatibilita se strukturou kanálů GSM pro snadné nasazení

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 45.913** (Rel-19) — Optimized Transmit Pulse Shape for EGPRS2-B
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity
- **TR 45.926** (Rel-19) — GERAN BTS Energy Saving Study

---

📖 **Anglický originál a plná specifikace:** [AFS na 3GPP Explorer](https://3gpp-explorer.com/glossary/afs/)
