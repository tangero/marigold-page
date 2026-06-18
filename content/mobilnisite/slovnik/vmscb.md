---
slug: "vmscb"
url: "/mobilnisite/slovnik/vmscb/"
type: "slovnik"
title: "VMSCB – Visited MSC of the B subscriber"
date: 2025-01-01
abbr: "VMSCB"
fullName: "Visited MSC of the B subscriber"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/vmscb/"
summary: "VMSCB (ústředna MSC navštívené sítě volaného účastníka B) je ústředna mobilního spojování (MSC) obsluhující volaného účastníka (účastníka B) v okruhově přepínaném hovoru. Jde o klíčovou funkční entitu"
---

VMSCB je ústředna mobilního spojování (Mobile Switching Center) obsluhující volaného účastníka v okruhově přepínaném hovoru, směruje hovory k roamujícím účastníkům a spravuje sestavování hovorů v sítích GSM/UMTS.

## Popis

VMSCB je prvek jádra sítě v okruhově přepínané doméně GSM a UMTS, konkrétně v podsystému přepínání sítě ([NSS](/mobilnisite/slovnik/nss/)). Je to [MSC](/mobilnisite/slovnik/msc/), které v daném okamžiku poskytuje službu účastníkovi B, tedy volané straně. Při zahájení hovoru (účastníkem A) musí proces směrování hovoru lokalizovat účastníka B, který může být mimo svou domovskou síť. Domovská síť účastníka B poskytne ze svého domovského registračního místa ([HLR](/mobilnisite/slovnik/hlr/)) směrovací informaci, která typicky obsahuje adresu VMSCB, jež tohoto účastníka aktuálně obsluhuje. VMSCB je zodpovědné za navázání spojení k terminálu účastníka B. Provádí paging k lokalizaci mobilní stanice ve své servisní oblasti, spravuje přidělování rádiových zdrojů pro hovor a zajišťuje signalizaci řízení hovoru. Také realizuje veškeré hovorové doplňkové služby (jako přesměrování či zákaz hovorů) podle profilu účastníka a komunikuje s dalšími síťovými entitami, jako je s ním asociovaný registrační místo návštěvy ([VLR](/mobilnisite/slovnik/vlr/)) pro data účastníka a bránová MSC ([GMSC](/mobilnisite/slovnik/gmsc/)) pro mezisíťové směrování.

Role VMSCB je klíčová ve fázi sestavování hovoru. Po přijetí hovorové žádosti od GMSC nebo jiné MSC ověří její platnost, zkontroluje místní stav a servisní profil účastníka B ze svého VLR a zahájí proces upozornění mobilní stanice. Spravuje zřízení hovorového kanálu (v GSM/UMTS) pro hlasovou komunikaci. Dále se VMSCB podílí na obsluze hovoru během jeho aktivního stavu, řídí aspekty jako předání hovoru (handover), pokud se účastník B pohybuje v jeho pokrytí, a je koncovým bodem větve hovoru směrem k účastníkovi B. Při ukončení hovoru uvolní zdroje a může generovat záznamy pro účtování.

V architektuře je VMSCB standardní MSC se všemi jejími typickými funkcemi: přepojování, řízení hovoru, správa mobility a propojení s jinými sítěmi. Jeho označení „Visited“ (navštívená) pouze naznačuje, že se nejedná o domovskou MSC účastníka; je to MSC v síti, kde účastník aktuálně roamuje. Písmeno „B“ specifikuje, že jde o volanou stranu. VMSCB spolupracuje s [VMSCA](/mobilnisite/slovnik/vmsca/) (Visited MSC of the A subscriber) pro volající stranu a celková cesta hovoru zahrnuje koordinaci mezi těmito ústřednami, případně přes GMSC. Jeho fungování je definováno v 3GPP TS 23.018 (základní obsluha hovorů) a TS 23.066 (podpora přenositelnosti mobilních čísel), což ilustruje jeho roli v základních i pokročilých scénářích směrování.

## K čemu slouží

Koncept VMSCB existuje, aby umožnil efektivní směrování a dokončení okruhově přepínaných hovorů k mobilním účastníkům, zejména když tito roamují. V raném systému GSM byla klíčovou výzvou lokalizace a připojení k účastníkovi, který mohl být kdekoli na světě. Domovská síť ([HLR](/mobilnisite/slovnik/hlr/)) zná údaje o účastníkovi, ale ne jeho aktuální polohu. VMSCB tento problém řeší tím, že je dynamicky přiřazeným kontaktním bodem v síti, kde se účastník fyzicky nachází. Poskytuje nezbytnou místní přepojovací a řídicí funkci pro rádiový přístup k dokončení hovoru.

Před existencí takto strukturované roamující architektury bylo volání mezi sítěmi obtížné nebo nemožné. VMSCB jako součást standardizované architektury [MSC](/mobilnisite/slovnik/msc/)/VLR/HLR umožňuje libovolné síti dotázat se domovského HLR, získat adresu aktuálně obsluhujícího MSC (VMSCB) a směrovat hovor přímo k němu. Tím se řeší problémy mobility účastníka a interoperability sítí. Také centralizuje řízení hovoru a provádění služeb pro volanou stranu v místě poskytování služby, což zajišťuje konzistentní aplikaci funkcí jako zákaz nebo přesměrování hovoru na základě profilu účastníka načteného z asociovaného VLR.

Motivací pro definování této konkrétní funkční role (VMSCB) ve standardech bylo objasnit postupy směrování hovorů a zodpovědnosti různých síťových entit v prostředí s více MSC a více sítěmi. Poskytuje jasný referenční bod v signalizačních diagramech a specifikacích protokolů pro místa, kde musí být provedeny určité akce (jako paging, alerting). Tato přesnost je nezbytná pro spolehlivou a škálovatelnou globální mobilní telefonii.

## Klíčové vlastnosti

- Slouží jako místní přepojovací a řídicí bod hovoru pro volaného (B) účastníka.
- Získává směrovací informace z HLR účastníka B prostřednictvím GMSC.
- Provádí paging a zřizování rádiového kanálu pro účastníka B.
- Realizuje hovorové doplňkové služby pro účastníka B na základě dat z VLR.
- Spravuje větev hovoru směrem k účastníkovi B, včetně předání hovoru (handover) během hovoru.
- Generuje záznamy pro účtování za segment hovoru, který obsluhuje.

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [GMSC – Gateway Mobile Services Switching Centre](/mobilnisite/slovnik/gmsc/)
- [VMSCA – Visited Mobile Switching Center of the A-subscriber](/mobilnisite/slovnik/vmsca/)

## Definující specifikace

- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1

---

📖 **Anglický originál a plná specifikace:** [VMSCB na 3GPP Explorer](https://3gpp-explorer.com/glossary/vmscb/)
