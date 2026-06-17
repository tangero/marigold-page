---
slug: "mss"
url: "/mobilnisite/slovnik/mss/"
type: "slovnik"
title: "MSS – Mobile Satellite Services"
date: 2025-01-01
abbr: "MSS"
fullName: "Mobile Satellite Services"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mss/"
summary: "3GPP definovaný rámec pro integraci satelitních přístupových sítí s pozemními mobilními sítěmi. Umožňuje globální pokrytí, kontinuitu služeb a všudypřítomnou konektivitu využitím satelitů jako uzlů mi"
---

MSS je 3GPP rámec pro integraci satelitních přístupových sítí s pozemními mobilními sítěmi za účelem poskytnutí globálního pokrytí a kontinuity služeb využitím satelitů jako mimozemských uzlů.

## Popis

Mobilní satelitní služby (MSS) v kontextu 3GPP odkazují na systémovou architekturu a protokoly, které umožňují satelitním komponentám poskytovat mobilní komunikační služby jako součást sítě 3GPP. Počínaje vydáním 12 se 3GPP začalo zabývat studiem a standardizací integrace satelitního přístupu jako typu mimozemské sítě (NTN). Satelitní komponentou může být geostacionární družice ([GEO](/mobilnisite/slovnik/geo/)), družice na střední oběžné dráze ([MEO](/mobilnisite/slovnik/meo/)) nebo družice na nízké oběžné dráze ([LEO](/mobilnisite/slovnik/leo/)) fungující jako uzel radiového přístupu, případně s regenerativní užitečnou zátěží na palubě (fungující jako základnová stanice) nebo s transparentní užitečnou zátěží (fungující jako průchozí relé).

Architektura zahrnuje satelitní rozhraní pro rádiové spojení, které připojuje uživatelské zařízení (UE) k satelitu. Satelit je následně připojen k pozemní bránové stanici, která je rozhraním k jádrové síti 5G Core (5GC) nebo Evolved Packet Core (EPC). Mezi klíčové technické výzvy, které se řeší, patří velmi dlouhé zpoždění šíření (zejména u GEO), vysoký Dopplerův jev (u LEO) a přerušovaná viditelnost. Specifikace 3GPP definují úpravy fyzické vrstvy (např. časový předstih, [HARQ](/mobilnisite/slovnik/harq/)), řízení rádiových zdrojů a procedury mobility, aby bylo možné se s těmito podmínkami vyrovnat.

Z pohledu sítě je satelit integrován jako 3GPP gNB (v 5G) nebo [eNB](/mobilnisite/slovnik/enb/) (v LTE) se specifickými charakteristikami. Jádrová síť s ním v zásadě nakládá jako s dalším přístupovým uzlem, i když může být informována o jeho vlastnostech NTN pro funkce jako služby založené na poloze nebo plánování tolerantní vůči zpoždění. Služba poskytuje širokoplošné pokrytí včetně námořních, leteckých a odlehlých pozemních oblastí a může být využita pro vysílání/vícebodové vysílání, propojovací spoje nebo přímou konektivitu se zařízením. Práce zahrnuje studie proveditelnosti až po detailní specifikace protokolů pro rádiový přístup a integraci s jádrovou sítí.

## K čemu slouží

Standardizace MSS v 3GPP byla motivována potřebou poskytnout bezproblémové, globální mobilní pokrytí mimo dosah pozemních buněčných věží. Tradiční mobilní sítě jsou omezeny na obydlené pevninské oblasti, což ponechává oceány, pouště a odlehlé regiony bez služeb. Satelity vždy nabízely širokoplošné pokrytí, ale historicky fungovaly prostřednictvím proprietárních, neintegrovaných systémů. Účelem 3GPP MSS je překlenout tuto mezeru vytvořením jednotného standardu, kde je satelitní přístup nativní součástí mobilní sítě.

Řeší omezení pouze pozemních sítí tím, že poskytuje kontinuitu služeb pro uživatele pohybující se mimo pokrytí buněčnou sítí, umožňuje Internet věcí (IoT) a komunikaci mezi stroji ([MTC](/mobilnisite/slovnik/mtc/)) v odlehlých oblastech a nabízí odolnost sítě a záložní řešení pro obnovu po havárii. Vytvoření standardů MSS umožňuje výrobcům zařízení a sítí vyrábět interoperabilní zařízení, snižovat náklady a složitost a umožňuje mobilním operátorům partnerství se satelitními operátory za účelem nabídky skutečně globálních služeb v rámci jediného předplatného a uživatelského zážitku.

## Klíčové vlastnosti

- Integrace satelitního přístupu jako 3GPP definované mimozemské sítě (NTN)
- Podpora různých satelitních oběžných drah (GEO, MEO, LEO) a typů užitečné zátěže (transparentní, regenerativní)
- Úpravy pro dlouhé zpoždění šíření, vysoký Dopplerův jev a přerušovanou viditelnost spoje
- Bezproblémová kontinuita služeb mezi pozemním a satelitním přístupem
- Umožňuje globální pokrytí pro hlasové, datové, IoT a vysílací služby
- Standardizovaná rozhraní umožňující satelitním sítím připojení k 5GC/EPC

## Definující specifikace

- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TR 36.763** (Rel-17) — NB-IoT/eMTC Support for Non-Terrestrial Networks
- **TR 36.791** (Rel-16) — E-UTRA 2.4 GHz TDD Band for US
- **TS 38.807** (Rel-16) — NR beyond 52.6 GHz Study
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TR 38.820** (Rel-16) — NR; 7-24 GHz Frequency Range Study
- **TS 38.821** (Rel-16) — NR Support for Non-Terrestrial Networks
- **TS 38.863** (Rel-19) — NR NTN RF and Co-existence Spec

---

📖 **Anglický originál a plná specifikace:** [MSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mss/)
