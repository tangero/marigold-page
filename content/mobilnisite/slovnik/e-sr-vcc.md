---
slug: "e-sr-vcc"
url: "/mobilnisite/slovnik/e-sr-vcc/"
type: "slovnik"
title: "E-SR-VCC – Emergency Single Radio Voice Call Continuity"
date: 2025-01-01
abbr: "E-SR-VCC"
fullName: "Emergency Single Radio Voice Call Continuity"
category: "Mobility"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/e-sr-vcc/"
summary: "Specifická podmnožina funkce SR-VCC (Single Radio Voice Call Continuity), která zajišťuje kontinuitu nouzového hlasového hovoru při přesunu UE ze sítě s přepojováním paketů (LTE/5G) do starší sítě s p"
---

E-SR-VCC je podmnožina SR-VCC, která zajišťuje, že nouzový hlasový hovor pokračuje bez přerušení, když se UE přesune ze sítě LTE/5G s přepojováním paketů do starší sítě 2G/3G s přepojováním okruhů, a to i v případě, že UE nemá platnou SIM kartu.

## Popis

Emergency Single Radio Voice Call Continuity (E-SR-VCC) je síťový postup mobility definovaný pro udržení aktivního nouzového hlasového hovoru v IP Multimedia Subsystem (IMS) při přesunu uživatelského zařízení (UE) z pokrytí sítě s podporou VoLTE (Voice over LTE) nebo VoNR a přepojováním paketů ([PS](/mobilnisite/slovnik/ps/)) do pokrytí starší sítě s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)), jako je GSM nebo UMTS. Hlavní výzvou je, že UE s jedním rádiovým transceiverem nemůže vysílat/přijímat na sítích PS a CS současně. E-SR-VCC umožňuje plynulé předání hovoru převedením nouzové IMS relace ukotvené v jádru PS do domény CS.

Procedura je spuštěna [E-UTRAN](/mobilnisite/slovnik/e-utran/) (nebo NG-RAN) na základě měřicích zpráv, které indikují zhoršující se sílu signálu LTE/5G a dostatečnou sílu cílové buňky CS. Pro nouzový hovor obslužný [MME](/mobilnisite/slovnik/mme/) (v EPC) nebo [AMF](/mobilnisite/slovnik/amf/) (v 5GC) identifikuje relaci jako nouzovou a vyvolá proceduru E-SR-VCC. Síť zahájí předání z PS do CS přes rozhraní Sv mezi MME/AMF a [MSC](/mobilnisite/slovnik/msc/) Serverem (rozšířeným pro [SR-VCC](/mobilnisite/slovnik/sr-vcc/)). Klíčovou komponentou je Emergency Access Transfer Control Function (E-ATCF), která slouží jako bod ukotvení kontinuity IMS služeb pro nouzový hovor. E-ATCF usnadňuje přenos relace interakcí s Emergency Call Session Control Function ([E-CSCF](/mobilnisite/slovnik/e-cscf/)).

Během provádění předání síť poskytne UE potřebné informace o CS kanálu. IMS relace je převedena pomocí mechanismů jako Session Transfer Initiation (STI) a Emergency Session Transfer Number (E-STN-SR), což je specifické číslo směrované na E-ATCF. Médiová cesta je přepnuta z přenašeče PS na přenašeč CS připojený k Media Gateway (MGW). Zásadní je, že procedury E-SR-VCC jsou povoleny i pro UE ve stavu omezené služby (např. bez platné SIM karty pro běžnou autentizaci), čímž je zajištěn univerzální přístup k nouzovým službám. Podrobné signalizační toky a požadavky jsou specifikovány v 3GPP TS 24.237.

## K čemu slouží

E-SR-VCC bylo standardizováno v 3GPP Release 9, aby vyřešilo kritickou mezeru v raných nasazeních LTE: absenci nativní domény hlasu s přepojováním okruhů. Zatímco SR-VCC bylo vyvinuto pro zajištění kontinuity běžných komerčních hovorů VoLTE, nouzové služby mají přísnější regulatorní a provozní požadavky. Orgány vyžadují, aby nouzové hovory byly možné z jakéhokoli zařízení, dokonce i bez aktivního předplatného (bez SIM karty), a musí být udržovány s vysokou spolehlivostí. Bez E-SR-VCC by byl nouzový hovor zřízený přes IMS v ostrově pokrytí LTE přerušen, jakmile by se UE přesunulo do oblasti pouze s 2G/3G, což by vytvořilo závažné riziko pro veřejnou bezpečnost.

Technologie byla motivována potřebou splnit regulatorní požadavky (např. požadavky FCC na E911) a zajistit, aby přechod na plně IP sítě LTE nezhoršil spolehlivost nouzových služeb ve srovnání se staršími CS sítěmi. Vyřešila problém udržení kontinuity nouzového hovoru pro UE, která nejsou plně registrována nebo autentizována pro běžné IMS služby. Definováním specifických postupů a síťových funkcí zaměřených na nouzové situace (jako je E-ATCF a použití E-STN-SR) E-SR-VCC zajistilo, že logika předání hovoru upřednostňuje nouzové relace a funguje i v podmínkách omezené služby, čímž plní 'záchrannou' povinnost mobilních sítí.

## Klíčové vlastnosti

- Zajišťuje kontinuitu nouzových hlasových hovorů založených na IMS při přechodu ze sítí LTE/5G do CS sítí 2G/3G.
- Funguje pro UE ve stavu omezené služby (např. bez platné UICC).
- Využívá funkci Emergency Access Transfer Control Function (E-ATCF) jako ukotvovací bod v IMS.
- Používá Emergency Session Transfer Number (E-STN-SR) pro směrování relace.
- Spoléhá na rozhraní Sv mezi MME/AMF a MSC Serverem pro koordinaci předání hovoru.
- Definuje specifické zpracování s prioritou pro nouzové relace během procedur SR-VCC.

## Související pojmy

- [SR-VCC – Single Radio Voice Call Continuity](/mobilnisite/slovnik/sr-vcc/)
- [E-STN-SR – Emergency Call Session Transfer Number – Single Radio](/mobilnisite/slovnik/e-stn-sr/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 24.237** (Rel-19) — IMS Service Continuity Protocol Details

---

📖 **Anglický originál a plná specifikace:** [E-SR-VCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-sr-vcc/)
