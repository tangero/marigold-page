---
slug: "eid"
url: "/mobilnisite/slovnik/eid/"
type: "slovnik"
title: "EID – Error Insertion Device"
date: 2025-01-01
abbr: "EID"
fullName: "Error Insertion Device"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/eid/"
summary: "Komponenta testovacího zařízení používaná při konformním a interoperabilním testování mobilních zařízení. Záměrně zavádí řízené chyby nebo zhoršení do komunikačních spojů, aby ověřila schopnost zaříze"
---

EID je komponenta testovacího zařízení používaná při konformním testování mobilních zařízení za účelem záměrného zavádění řízených chyb do komunikačních spojů a ověření schopnosti zařízení zpracovat chyby a robustnosti protokolu.

## Popis

Error Insertion Device (EID, zařízení pro vkládání chyb) je specializovaná komponenta testovacího zařízení používaná primárně v laboratorních a certifikačních testovacích prostředích pro uživatelská zařízení (UE). Její hlavní funkcí je simulace reálných, nedokonalých přenosových podmínek záměrným vkládáním chyb do komunikačního kanálu mezi UE a testovacím systémem (např. emulátorem základnové stanice). To je klíčové pro ověření, že UE správně a robustně implementuje procedury protokolu, zejména její schopnost detekovat chyby, vyžádat si retransmise a obnovit se z chyb bez pádu nebo projevu nedefinovaného chování.

EID pracuje na různých vrstvách protokolu v závislosti na testovacím případu. Například může poškodit bity v transportních blocích fyzické vrstvy, zavést chyby do hlaviček [MAC](/mobilnisite/slovnik/mac/) vrstvy, simulovat ztráty RLC protokolových datových jednotek (PDU) nebo poškodit PDCP či [RRC](/mobilnisite/slovnik/rrc/) zprávy. Chyby jsou vkládány řízeným a opakovatelným způsobem podle specifikací 3GPP testů (jako jsou ty v řadě 36.5xx pro LTE RF konformní testy). Testovací systém nakonfiguruje EID parametry definující vzor chyby, míru vkládání a cílovou vrstvu nebo kanál. Reakce UE jsou následně monitorovány a hodnoceny vůči očekávanému chování definovanému v protokolových standardech.

Mezi klíčové specifikace odkazující na funkčnost EID patří TS 26.935 (pro testování řečových kodeků), TS 26.969 (pro testování vylepšených hlasových služeb) a starší 3GPP TS 46.008 a TS 46.085 (které detailně popisují testovací procedury pro GSM, kde byl tento koncept také používán). Použitím EID mohou testovací inženýři ověřit kritické funkce jako je provoz Hybrid Automatic Repeat Request ([HARQ](/mobilnisite/slovnik/harq/)), retransmise v RLC Acknowledged Mode ([AM](/mobilnisite/slovnik/am/)), detekce selhání rádiového spoje a provedení handoveru za podmínek se ztrátami. To zajišťuje, že UE nasazená v komerčních sítích budou spolehlivě fungovat i přes přerušované rušení, útlum nebo ztrátu paketů.

## K čemu slouží

Error Insertion Device existuje pro umožnění důkladného, standardizovaného testování odolnosti mobilních zařízení a shody s protokolem. V reálném nasazení jsou bezdrátové kanály inherentně nespolehlivé kvůli rušení, vícecestnému útlumu a mobilitě. UE musí být schopno tyto nedokonalosti elegantně zvládat. Účelem EID je vytvořit laboratorně řízené prostředí, které reprodukovatelně napodobuje tyto nepříznivé podmínky, které by bylo obtížné nebo nemožné spolehlivě vytvořit pouze pomocí poruch na rádiové frekvenci přenášených vzduchem.

Řeší potřebu objektivního, vyhodnoceného jako vyhovující/nevyhovující konformního testování, jak jej definují certifikační orgány jako Global Certification Forum ([GCF](/mobilnisite/slovnik/gcf/)) a PTCRB. Bez EID by bylo náročné ověřit, že UE správně implementuje povinné procedury obnovy po chybě specifikované v 3GPP protokolech. Jeho použití zajišťuje interoperabilitu mezi zařízeními od různých výrobců a sítěmi různých operátorů, protože všechna certifikovaná zařízení prokázala schopnost zpracovat společnou sadu chybových scénářů standardizovaným způsobem. To nakonec zlepšuje stabilitu sítě a uživatelský zážitek snížením výskytu přerušených hovorů, zamrzlých datových relací a dalších selhání způsobených špatným zpracováním chyb.

## Klíčové vlastnosti

- Vkládá řízené, reprodukovatelné chyby do komunikačního spoje během testování
- Pracuje na určených vrstvách protokolu (např. fyzická vrstva, RLC vrstva)
- Konfigurovatelné vzory chyb, míry vkládání a cílové kanály
- Nezbytný pro konformní testování procedur obnovy po chybě u UE
- Používá se k validaci mechanismů HARQ, ARQ a detekce selhání rádiového spoje
- Podporován specifikacemi 3GPP testů pro zajištění standardizované testovací metodologie

## Související pojmy

- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TR 26.969** (Rel-19) — eCall In-band Modem Performance Characterization
- **TS 46.008** (Rel-19) — GSM Half Rate Speech Codec Performance
- **TS 46.085** (Rel-19) — GSM Speech Codec Interoperability Test Report

---

📖 **Anglický originál a plná specifikace:** [EID na 3GPP Explorer](https://3gpp-explorer.com/glossary/eid/)
