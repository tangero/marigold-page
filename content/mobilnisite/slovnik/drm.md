---
slug: "drm"
url: "/mobilnisite/slovnik/drm/"
type: "slovnik"
title: "DRM – Data call Routeing Mechanism"
date: 2025-01-01
abbr: "DRM"
fullName: "Data call Routeing Mechanism"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/drm/"
summary: "Mechanismus jádrové sítě v GSM a UMTS, který určuje optimální směrovací cestu pro mobilním zařízením iniciovaný datový hovor (např. okruhově přepínaný datový nebo faxový hovor). Zahrnuje interakce mez"
---

DRM je mechanismus jádrové sítě v GSM a UMTS, který určuje optimální směrovací cestu pro mobilním zařízením iniciované okruhově přepínané datové nebo faxové hovory.

## Popis

Data call Routeing Mechanism (DRM) je zastaralá funkce jádrové sítě definovaná v raných vydáních 3GPP pro okruhově přepínanou ([CS](/mobilnisite/slovnik/cs/)) doménu GSM a UMTS. Řídí navázání a směrování mobilním zařízením iniciovaných datových a faxových hovorů, které se odlišují od hlasových hovorů potřebou specifických funkcí pro vzájemné propojení ([IWF](/mobilnisite/slovnik/iwf/)). Když mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) zahájí datový nebo faxový hovor, obsluhující ústředna mobilního přepínače ([MSC](/mobilnisite/slovnik/msc/)) musí určit, jak tento hovor připojit k externí datové síti (jako je PSTN/[ISDN](/mobilnisite/slovnik/isdn/) nebo paketová datová síť přes IWF). DRM je standardizovaný postup, který tento rozhodovací proces umožňuje.

Mechanismus funguje prostřednictvím série dotazů a výměn informací mezi síťovými entitami. Po přijetí žádosti o navázání datového hovoru obsluhující MSC analyzuje volané číslo a informační prvek přenosové schopnosti poskytnutý MS. MSC pak typicky dotazuje návštěvnické registrační středisko (VLR) o data specifická pro účastníka. Zásadně může DRM zahrnovat dotazování domovského registračního střediska ([HLR](/mobilnisite/slovnik/hlr/)) za účelem získání informací o směrování datových hovorů účastníka, které mohou zahrnovat preference nebo omezení. Na základě těchto shromážděných informací – včetně typu požadované datové služby (např. asynchronní data, fax), profilu účastníka a konfigurace sítě – MSC spustí logiku DRM, aby vybrala optimální výstupní bod z PLMN. To často znamená výběr konkrétní jednotky funkce pro vzájemné propojení (IWF), která může být integrována v rámci MSC (MSCIWF) nebo může být samostatným uzlem, aby provedla nezbytnou adaptaci protokolu, adaptaci přenosové rychlosti a převod modulace (např. z modemových zvukových tónů na digitální datové toky).

Architektura DRM je zabudována do protokolů jádrové sítě CS, především v signalizaci [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part) mezi MSC, VLR a HLR a v procedurách řízení hovoru (např. TS 24.008). Její role byla klíčová v éře okruhově přepínaných datových služeb (jako [CSD](/mobilnisite/slovnik/csd/) a HSCSD) a faxových služeb, protože zajišťovala, že tyto hovory byly směrovány k síťovým uzlům vybaveným správnými modemy a schopnostmi vzájemného propojení. S přechodem odvětví na sítě typu all-IP a převahou paketově přepínaných dat (GPRS, EPS, 5GS) se praktický význam DRM výrazně snížil, protože datové služby jsou nyní nativně paketové a nevyžadují okruhově přepínané vzájemné propojení stejným způsobem.

## K čemu slouží

DRM byl vyvinut k řešení problému efektivního směrování okruhově přepínaných datových a faxových hovorů v raných digitálních mobilních sítích (GSM). Na rozdíl od hlasových hovorů, které mohly být směrovány přes standardní trunky PSTN, datové/faxové hovory vyžadovaly specifické koncové zařízení (modemy) a funkce vzájemného propojení pro převod mezi protokoly digitální mobilní sítě a analogovými modemovými signály používanými na PSTN nebo digitálními protokoly ISDN. Bez standardizovaného mechanismu existovalo riziko nesprávného směrování hovorů k síťovým uzlům postrádajícím požadované schopnosti IWF, což vedlo k selhání navázání hovoru nebo špatné kvalitě.

Vytvoření DRM poskytlo standardizovaný proces rozhodování o směrování, který zohledňuje účastníka. Umožnil síťovým operátorům konfigurovat flexibilní směrovací politiky na základě typu služby, předplatného účastníka (např. někteří účastníci mohli být omezeni na určité datové služby) a topologie sítě. Tím bylo zajištěno spolehlivé navázání hovoru pro služby s přidanou hodnotou, jako je fax a vytáčené datové připojení, které byly důležitými obchodními službami v 90. letech a na počátku 21. století. Řešil omezení plynoucí z toho, že se se všemi okruhově přepínanými hovory zacházelo stejně, a byl nezbytnou součástí kompletní nabídky služeb sítí 2G a raných 3G před rozšířeným přijetím trvale připojených paketových dat.

## Klíčové vlastnosti

- Určuje směrování pro mobilním zařízením iniciované okruhově přepínané datové/faxové hovory.
- Zahrnuje signalizaci mezi MSC, VLR a HLR.
- Vybere příslušnou funkci pro vzájemné propojení (IWF) na základě typu služby.
- Zohledňuje profil účastníka a informace o přenosové schopnosti.
- Je integrován s protokoly MAP a řízení hovoru.
- Podporuje zastaralé služby jako CSD, HSCSD a fax.

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [IWF – InterWorking Function](/mobilnisite/slovnik/iwf/)

## Definující specifikace

- **TS 22.242** (Rel-19) — DRM Service Requirements
- **TS 23.054** (Rel-4) — Shared Interworking Function (SIWF) Stage 2
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 23.844** (Rel-12) — IMS P2P Content Distribution Services Study
- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.233** (Rel-15) — 3GPP Packet-Switched Streaming Service (PSS)
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.841** (Rel-19) — Study on Media Messaging Enhancements
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TR 26.981** (Rel-19) — MBMS Provisioning & Content Ingestion Interface Study
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [DRM na 3GPP Explorer](https://3gpp-explorer.com/glossary/drm/)
