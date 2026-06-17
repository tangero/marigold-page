---
slug: "4pam"
url: "/mobilnisite/slovnik/4pam/"
type: "slovnik"
title: "4PAM – 4 Pulse-Amplitude Modulation"
date: 2025-01-01
abbr: "4PAM"
fullName: "4 Pulse-Amplitude Modulation"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/4pam/"
summary: "4PAM je digitální modulační schéma využívající čtyři různé úrovně amplitudy k zakódování dvou bitů na symbol, čímž zdvojnásobuje datový tok ve srovnání s binárními schématy, jako je BPSK, při dané šíř"
---

4PAM je digitální modulační schéma, které využívá čtyři různé úrovně amplitudy k zakódování dvou bitů na symbol, čímž zdvojnásobuje datový tok ve srovnání s binárními schématy při dané šířce pásma.

## Popis

4 Pulse-Amplitude Modulation (4PAM) je lineární digitální modulační technika zásadní pro fyzickou vrstvu systémů 3GPP UMTS/HSDPA. Funguje tak, že mapuje dvojice binárních bitů (dibity) na jednu ze čtyř diskrétních úrovní amplitudy nosného signálu. Konkrétně je vstupní bitový proud seskupen do dvoubitových symbolů (00, 01, 10, 11), z nichž každému je přiřazena specifická hodnota napětí nebo amplitudy (např. -3A, -A, +A, +3A). Tento symbol je pak použit k modulaci amplitudy tvarovaného impulsu, obvykle s využitím kořenového kosinusového filtru k omezení šířky pásma a minimalizaci intersymbolového rušení (ISI). Výsledný signál je přenášen přes rádiový kanál, kde v přijímači detektor vzorkuje signál a rozhodne, která ze čtyř úrovní amplitudy byla vyslána, a zpětně ji demapuje na původní dvoubitový symbol.

Architektura implementující 4PAM je zabudována do vysílače Node B a přijímače uživatelského zařízení (UE) pro High-Speed Physical Downlink Shared Channel (HS-PDSCH) v HSDPA. Klíčové komponenty zahrnují mapovač symbolů, který provádí mapování bitů na amplitudu; filtr pro tvarování impulsu; modulátor, který násobí tvarovaný impuls s nosnou frekvencí; a výkonový zesilovač. V přijímači jsou kritickými prvky přizpůsobený filtr (odpovídající tvaru vysílaného impulsu), vzorkovač na symbolové rychlosti a rozhodovací zařízení, často implementované jako detektor s třemi prahy pro rozlišení čtyř úrovní. Odhad kanálu a ekvalizace jsou také zásadní pro potlačení zkreslení amplitudy způsobeného vícecestným únikem.

Úloha 4PAM v síti je především zvýšit kapacitu dat na downlinku. Přenosem dvou bitů na symbol efektivně zdvojnásobuje spektrální účinnost ve srovnání s binární fázovou manipulací (BPSK), která přenáší jeden bit na symbol. To je využito v modulaci 16-QAM pro HSDPA, kde je 4PAM aplikováno nezávisle na fázové (I) a kvadraturní (Q) složce, což vede k 16 možným symbolovým stavům (4 amplitudy na I × 4 amplitudy na Q). 4PAM je však náchylnější k šumu a rušení než binární schémata, protože rozdíly amplitud mezi úrovněmi jsou menší, což vyžaduje vyšší poměr signálu k šumu (SNR) pro spolehlivou detekci. Jeho použití je proto typicky omezeno na dobré podmínky kanálu, přičemž adaptivní modulace a kódování (AMC) dynamicky přepíná na robustnější schémata, jako je QPSK, když je to potřeba.

Z pohledu systému integrace 4PAM zahrnuje těsnou koordinaci s dalšími procesy fyzické vrstvy. Indikátor kvality kanálu (CQI) hlášený UE pomáhá Node B rozhodnout, zda použít 16-QAM založenou na 4PAM. Řízení výkonu musí být přesné, aby byla zachována věrnost amplitudy, a přijímací algoritmy musí přesně odhadnout zesílení kanálu, aby správně škálovaly přijímané amplitudy. Jeho implementace je specifikována v 3GPP TS 25.211 pro fyzické kanály a TS 25.213 pro rozprostření a modulaci, což zajišťuje interoperabilitu napříč sítěmi UMTS.

## K čemu slouží

4PAM bylo zavedeno jako odpověď na rostoucí poptávku po vyšších datových tocích v mobilních sítích, konkrétně v rámci vývoje UMTS. Před HSDPA v Release 5 používal UMTS downlink modulaci QPSK, která je robustní, ale omezená na 2 bity na symbol (1 bit na I a Q složku). Jak rostla očekávání uživatelů vůči službám podobným širokopásmovým (např. streamování videa, stahování velkých souborů), tato spektrální účinnost se stala úzkým hrdlem. 4PAM jako součást 16-QAM bylo vyvinuto ke zdvojnásobení bitů na symbol, čímž se zvýšily špičkové datové toky bez rozšíření přiděleného pásma – což je klíčové s ohledem na nedostatek a cenu rádiového spektra.

Historický kontext spočívá v konkurenčním tlaku na technologie 3,5G. Zatímco Release 5 zavedlo HSDPA s QPSK a 16-QAM (s použitím 4PAM na každé ose), Release 7 jej dále optimalizovalo. Omezením dřívějších přístupů byl kompromis mezi datovým tokem a odolností spoje: binární modulace (BPSK) nebo QPSK nabízely dobrou odolnost proti šumu, ale nižší propustnost. 4PAM umožnilo vyšší řád modulace (16-QAM) využívat dobré podmínky kanálu blízko středu buňky, kde je SNR vysoké. Tento adaptivní přístup v kombinaci s hybridním ARQ a rychlým plánováním umožnil sítím dynamicky maximalizovat propustnost, čímž se zlepšila celková kapacita systému a uživatelský zážitek.

Navíc 4PAM řešilo problém efektivního využití vylepšených přijímacích schopností v novějších UE. Jak zařízení začala obsahovat lepší ekvalizéry a pokročilé zpracování signálu, mohla spolehlivě dekódovat více úrovní amplitudy. 4PAM poskytlo standardizované modulační schéma pro využití těchto pokroků a zajištění zpětné kompatibility – UE nepodporující 16-QAM mohla přepnout zpět na QPSK. Toto přírůstkové vylepšení umožnilo operátorům zvýšit výkon sítě s existujícím spektrem, oddálit nákladné akvizice spektra nebo dělení buněk, a tím optimalizovat kapitálové výdaje při současném uspokojení rostoucích datových požadavků.

## Klíčové vlastnosti

- Kóduje dva bity na symbol pomocí čtyř úrovní amplitudy
- Zdvojnásobuje spektrální účinnost ve srovnání s binárními modulačními schématy, jako je BPSK
- Tvoří základ pro modulaci 16-QAM, když je aplikováno nezávisle na I a Q složkách
- Vyžaduje pro spolehlivou detekci vyšší poměr signálu k šumu (SNR) než QPSK
- Používá se adaptivně v HSDPA na základě indikátorů kvality kanálu (CQI)
- Specifikováno ve 3GPP pro HS-PDSCH za účelem zvýšení propustnosti na downlinku

## Definující specifikace

- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation

---

📖 **Anglický originál a plná specifikace:** [4PAM na 3GPP Explorer](https://3gpp-explorer.com/glossary/4pam/)
