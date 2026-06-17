---
slug: "moho"
url: "/mobilnisite/slovnik/moho/"
type: "slovnik"
title: "MOHO – Mobile Originated Handover"
date: 2025-01-01
abbr: "MOHO"
fullName: "Mobile Originated Handover"
category: "Mobility"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/moho/"
summary: "Procedura předání spojení iniciovaná mobilní stanicí (MS) nebo uživatelským zařízením (UE), typicky na základě jeho vlastních rádiových měření, za účelem žádosti o přenos na novou buňku nebo kanál. Jd"
---

MOHO je procedura předání spojení iniciovaná mobilní stanicí na základě vlastních rádiových měření za účelem žádosti o přenos na novou buňku pro optimalizované udržení spojení.

## Popis

Mobile Originated Handover (MOHO) je specifický typ procedury předání spojení v celulárních sítích, kde iniciativa ke spuštění předání vychází z mobilního zařízení ([MS](/mobilnisite/slovnik/ms/) v GSM/UMTS, UE v LTE/5G), na rozdíl od sítě (Network Originated Handover). UE průběžně provádí měření na obsluhující buňce a sousedních buňkách podle konfigurace od sítě prostřednictvím zpráv řízení měření. Když vnitřní algoritmy UE určí, že předání je nutné nebo prospěšné – například kvůli zhoršující se kvalitě signálu z aktuální buňky nebo výrazně silnějšímu signálu od souseda – může odeslat měřicí hlášení síti se specifickou indikací nebo, v některých implementacích systémů, explicitně požádat o předání.

Technický proces zahrnuje fyzickou a protokolovou vrstvu UE. Vrstva 1 (fyzická vrstva) UE měří výkon přijímaného referenčního signálu (RSRP), kvalitu přijímaného referenčního signálu (RSRQ) v LTE/5G nebo výkon přijímaného signálového kódu (RSCP) v UMTS. Tato měření zpracovává vrstva řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) UE. Na základě nastavených prahových hodnot a parametrů hystereze přijatých od sítě se entita RRC v UE rozhodne, zda má být odesláno měřicí hlášení spouštěné událostí. Pro MOHO může toto hlášení obsahovat doporučení pro konkrétní cílovou buňku. Po přijetí tohoto hlášení učiní RAN uzel sítě (např. eNodeB, gNB) konečné rozhodnutí, přičemž zváží další faktory, jako je zatížení sítě a řízení přístupu, než provede fáze přípravy a provedení předání s cílovou buňkou.

MOHO je kritickou součástí schémat předání spojení s asistencí UE a řízením sítí. Přesouvá část procesní zátěže a iniciativy rozhodnutí na UE, které má přímé a okamžité povědomí o rádiovém prostředí. To může vést k rychlejším reakcím na rychlé útlumy signálu. Síť si zachovává konečnou kontrolu, aby zajistila celkovou stabilitu a optimalizaci zdrojů. Mezi klíčové komponenty umožňující MOHO patří měřicí schopnosti UE, protokol RRC pro hlášení a konfigurace měření sítě a algoritmy pro rozhodování o předání. V pokročilých systémech jsou principy MOHO základem pro funkce jako podmíněné předání spojení ([CHO](/mobilnisite/slovnik/cho/)) v 5G, kde je UE předkonfigurováno podmínkami pro předání.

## K čemu slouží

MOHO bylo vyvinuto za účelem zlepšení spolehlivosti a efektivity předání spojení v dynamickém rádiovém prostředí. V raných celulárních systémech byla předání spojení primárně iniciována sítí na základě měření hlášených základnovými stanicemi, což nemuselo plně zachytit rychlé změny signálu, které zažívá rychle se pohybující mobilní zařízení. To mohlo vést k přerušeným hovorům nebo suboptimální konektivitě. MOHO zmocňuje UE, entitu přímo zažívající rádiový spoj, aby proaktivně iniciovala proces předání, čímž se snižuje latence při reakci na zhoršující se podmínky.

Tato technologie řeší problém zpoždění předání a "ping-pong" efektů v hraničních oblastech. Tím, že umožňuje UE spouštět předání na základě svých přesných měření, může k předání dojít dříve, než kvalita spojení klesne pod použitelnou mez, čímž se zlepšuje míra přerušení hovorů. Je zvláště cenná ve scénářích s malými buňkami nebo vysokou mobilitou uživatelů, kde se rádiové podmínky rychle mění. MOHO také přispívá k celkovému výkonu sítě tím, že usnadňuje vyvažování zatížení; UE, které zažívá přetížení ve své aktuální buňce, může požádat o předání na méně zatíženého souseda, což je aspekt, který se vyvinul v pozdějších standardech.

Historicky bylo předání spojení přísně řízeným procesem sítě. Zavedení MOHO, zejména od dob GSM/UMTS, představovalo posun směrem k distribuovanější správě mobility. Uznávalo UE jako inteligentního agenta v síti. Tento koncept položil základy pro stále více uživatelským zařízením (UE) centrickou mobilitu v 4G a 5G, jako je autonomní vyhledávání a měření UE, a nakonec podmíněné předání spojení, kde UE samo provede předání při splnění podmínek definovaných sítí, čímž se minimalizuje signalizační zpoždění a zvýší robustnost.

## Klíčové vlastnosti

- Spouštěč předání spojení iniciovaný uživatelským zařízením (UE)
- Založeno na měřeních obsluhující a sousedních buněk provedených UE
- UE odesílá měřicí hlášení s potenciálními doporučeními pro předání
- Konečné rozhodnutí o předání a pravomoc jeho provedení zůstává síti
- Snižuje latenci předání využitím reálného povědomí UE o rádiovém stavu
- Základ pro pokročilá schémata mobility, jako je podmíněné předání spojení

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding

---

📖 **Anglický originál a plná specifikace:** [MOHO na 3GPP Explorer](https://3gpp-explorer.com/glossary/moho/)
