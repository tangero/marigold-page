---
slug: "seaq"
url: "/mobilnisite/slovnik/seaq/"
type: "slovnik"
title: "SEAQ – System for the Evaluation of Audio Quality"
date: 2025-01-01
abbr: "SEAQ"
fullName: "System for the Evaluation of Audio Quality"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/seaq/"
summary: "SEAQ je standardizovaný systém 3GPP pro objektivní hodnocení zvukové kvality řečových kodeků a hlasových služeb v mobilních sítích. Poskytuje rámec pro provádění poslechových testů a analýzu výsledků"
---

SEAQ je standardizovaný systém 3GPP pro objektivní hodnocení zvukové kvality řečových kodeků a hlasových služeb v mobilních sítích prostřednictvím rámce poslechových testů a analýzy.

## Popis

Systém pro hodnocení zvukové kvality (SEAQ) je komplexní metodologie definovaná v dokumentu 3GPP TS 26.936 pro subjektivní a objektivní posouzení kvality řeči a zvuku v telekomunikačních systémech. Stanovuje standardizované postupy pro provádění poslechových testů, které zahrnují lidské subjekty hodnotící zpracované vzorky řeči v kontrolovaných podmínkách. Tyto testy generují střední hodnoty uživatelského hodnocení ([MOS](/mobilnisite/slovnik/mos/)) nebo jiné percepční metriky, které kvantifikují zvukovou kvalitu tak, jak ji vnímá koncový uživatel. Systém zahrnuje podrobné pokyny pro nastavení testovacího prostředí, včetně akustických požadavků na poslechové místnosti, kalibrace přehrávací techniky a výběru reprezentativního řečového materiálu a podmínek okolního hluku.

SEAQ funguje tak, že definuje konkrétní testovací metodologie, jako je Absolutní kategorické hodnocení ([ACR](/mobilnisite/slovnik/acr/)), Degradační kategorické hodnocení ([DCR](/mobilnisite/slovnik/dcr/)) a Srovnávací kategorické hodnocení ([CCR](/mobilnisite/slovnik/ccr/)), pro měření různých aspektů zvukové kvality. Proces spočívá v přehrávání zpracovaných řečových vzorků – které mohly projít kompresí kodeku, maskováním ztráty paketů nebo jinými síťovými znehodnoceními – panelu posluchačů, kteří kvalitu hodnotí na standardizovaných škálách. Na sebraná hodnocení je následně aplikována statistická analýza za účelem vytvoření spolehlivých skóre kvality s intervaly spolehlivosti. Systém se také zabývá školením posluchačů, testováním sluchových vad a použitím referenčních podmínek pro zajištění konzistence testů a reprodukovatelnosti napříč různými laboratořemi a testovacími organizacemi.

Klíčové součásti SEAQ zahrnují vedoucího testu, který navrhuje a dohlíží na hodnocení, poslechový panel složený ze školených nebo neškolených subjektů v závislosti na použité metodě, přehrávací systém s přesně kalibrovanou zvukovou technikou a databázi řečového materiálu obsahující standardizované nahrávky v různých jazycích. Systém definuje konkrétní podmínky znehodnocení simulující reálné síťové scénáře, jako jsou různé přenosové rychlosti, vymazání rámců, zpoždění a tandemová kódování. Role SEAQ v síťovém ekosystému je klíčová pro ověření, že řečové kodeky (jako [AMR](/mobilnisite/slovnik/amr/), [EVS](/mobilnisite/slovnik/evs/) nebo budoucí kodeky) a hlasové služby (VoLTE, VoNR) splňují kvalitativní požadavky před jejich nasazením, čímž zajišťují interoperabilitu a konzistentní uživatelský zážitek napříč různými síťovými implementacemi a výrobci zařízení.

## K čemu slouží

SEAQ byl vytvořen pro uspokojení potřeby standardizované, spolehlivé a opakovatelné metody hodnocení percepční zvukové kvality řečových kodeků a hlasových služeb v mobilních sítích. Před jeho standardizací různí výrobci zařízení a síťoví operátoři často používali proprietární testovací metodologie, což ztěžovalo objektivní srovnání výkonu kodeků nebo zaručení konzistentní hlasové kvality napříč interoperabilními systémy. Tento nedostatek standardizace mohl vést k nesrovnalostem v hodnocení kvality, což bránilo výběru optimálních kodeků pro síťové nasazení a mohlo potenciálně degradovat zážitek koncového uživatele v prostředích s více dodavateli.

Tato technologie řeší problém subjektivního hodnocení kvality tím, že poskytuje jednotný rámec zajišťující provádění testů za vědecky kontrolovaných podmínek a produkující výsledky, které jsou statisticky platné a srovnatelné napříč různými testovacími příležitostmi a laboratořemi. Řeší výzvu posouzení, jak si kodeky vedou při realistických síťových znehodnoceních – jako je ztráta paketů, kolísání zpoždění (jitter) a variace šířky pásma – které významně ovlivňují vnímanou kvalitu, ale je obtížné je přesně modelovat bez standardizovaných testovacích podmínek. SEAQ umožňuje 3GPP činit informovaná rozhodnutí během standardizace kodeků tím, že poskytuje empirické důkazy o kvalitě za různých provozních scénářů.

Historicky, jak se mobilní sítě vyvíjely z 2G přes 3G a dále a zaváděly nové širokopásmové a plnopásmové kodeky, rostla složitost hodnocení kvality. SEAQ poskytl potřebnou metodologii pro ověření, že tyto pokročilé kodeky (např. [AMR-WB](/mobilnisite/slovnik/amr-wb/), [EVS](/mobilnisite/slovnik/evs/)) skutečně přinášejí slibované zlepšení kvality oproti starším úzkopásmovým kodekům. Také podporuje hodnocení kvality nově vznikajících služeb, jako je Voice over LTE (VoLTE) a Voice over NR (VoNR), kde přenos s přepojováním paketů přináší nové faktory znehodnocení kvality, se kterými se přenos s přepojováním okruhů nesetkával.

## Klíčové vlastnosti

- Standardizované metodologie pro subjektivní poslechové testy (ACR, DCR, CCR)
- Podrobné specifikace pro akustiku testovacího prostředí a kalibraci zařízení
- Pokyny pro výběr a školení poslechových panelů
- Postupy pro statistickou analýzu výsledků s intervaly spolehlivosti
- Definice reprezentativního řečového materiálu a podmínek okolního hluku
- Podpora testování za různých scénářů síťového znehodnocení

## Definující specifikace

- **TR 26.936** (Rel-19) — Audio Codec Characterization Technical Report

---

📖 **Anglický originál a plná specifikace:** [SEAQ na 3GPP Explorer](https://3gpp-explorer.com/glossary/seaq/)
