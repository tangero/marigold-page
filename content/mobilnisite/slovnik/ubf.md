---
slug: "ubf"
url: "/mobilnisite/slovnik/ubf/"
type: "slovnik"
title: "UBF – UE Beam Lock Function"
date: 2024-01-01
abbr: "UBF"
fullName: "UE Beam Lock Function"
category: "Radio Access Network"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/ubf/"
summary: "Schopnost UE v NR, která umožňuje zařízení zamknout se na konkrétní paprsek od gNB, čímž se snižuje režie správy paprsků a zlepšuje výkon mobility. Pomáhá udržovat stabilní konektivitu ve scénářích s"
---

UBF je schopnost UE v NR, která umožňuje zařízení zamknout se na konkrétní paprsek gNB, aby se snížila režie správy a zlepšil výkon mobility ve scénářích s beamformingem na vysokých frekvencích.

## Popis

Funkce zamknutí paprsku UE (UE Beam Lock Function, UBF) je vlastnost definovaná ve specifikacích 3GPP New Radio (NR), zejména pro provoz ve frekvenčních pásmech nad 6 GHz (FR2), kde je beamforming zásadní kvůli vysokým útlumům na dráze a směrovému šíření. UBF umožňuje uživatelskému zařízení (UE) zamknout se na konkrétní paprsek vysílaný gNB (next-generation NodeB), což znamená, že UE preferenčně používá tento paprsek pro uplinkovou a downlinkovou komunikaci, dokud určité podmínky nespustí změnu paprsku. Tato funkce je součástí širšího rámce správy paprsků, který zahrnuje procedury měření, hlášení a přepínání paprsků.

V praxi UBF funguje tak, že UE sleduje kvalitu zamčeného paprsku (např. pomocí [RSRP](/mobilnisite/slovnik/rsrp/) nebo [SINR](/mobilnisite/slovnik/sinr/) ze SSB nebo [CSI-RS](/mobilnisite/slovnik/csi-rs/)). UE může být nakonfigurována prahovými hodnotami nebo časovači, aby určila, kdy zámek uvolnit a zahájit obnovu paprsku nebo hledání lepšího paprsku. gNB může tento proces také ovlivňovat pomocí signalizace [RRC](/mobilnisite/slovnik/rrc/) nebo [MAC](/mobilnisite/slovnik/mac/) Control Elements (MAC-CEs), což poskytuje flexibilitu v síťově řízené versus autonomní správě paprsků na straně UE.

Klíčové součásti zahrnují fyzickou vrstvu a vrstvu MAC v UE, které zpracovávají logiku měření a zamknutí paprsku, a beamformingové a plánovací funkce gNB. UBF snižuje frekvenci přepínání paprsků, což minimalizuje signalizační režii a potenciální přerušení, zejména ve scénářích mobility, kdy se UE pohybuje, ale optimální paprsek se může rychle měnit. Přispívá k efektivnějšímu využití síťových zdrojů a lepší uživatelské zkušenosti tím, že udržuje stabilní spojení pomocí paprsku, čímž zvyšuje propustnost a spolehlivost v milimetrových vlnách.

## K čemu slouží

UBF byla zavedena, aby řešila výzvy v správě paprsků v NR, zejména ve vysokofrekvenčních pásmech (např. mmWave), kde jsou paprsky úzké a vysoce směrové. Bez zamknutí paprsku by UE mohly často přepínat paprsky v reakci na malé výkyvy signálu, což by vedlo k nadměrné signalizační režii, zvýšené latenci a potenciální nestabilitě spojení. To je zvláště problematické ve scénářích mobility, kde rychlé změny paprsků mohou degradovat výkon a vybíjet baterii UE kvůli neustálému měření a hlášení.

Před UBF se správa paprsků silně opírala o periodické měření a hlášení paprsků, což mohlo být v dynamickém prostředí neefektivní. Tato funkce poskytuje mechanismus pro stabilizaci výběru paprsku, snižuje zbytečné přepínání paprsků a umožňuje síti i UE šetřit zdroje. Řeší problém 'ping-pongu paprsků', kdy UE osciluje mezi paprsky, a zlepšuje tak výkon přechodu mezi buňkami a celkovou efektivitu systému.

Motivace vychází z potřeby učinit komunikaci v milimetrových vlnách praktickou pro mobilní případy použití, jak je definováno ve 3GPP Release 15 a vylepšeno v následujících vydáních. Tím, že umožňuje UE zamknout se na paprsek, UBF podporuje spolehlivou mobilitu a konzistentní QoS, což je klíčové pro aplikace jako eMBB a [URLLC](/mobilnisite/slovnik/urllc/) v 5G sítích. Představuje vývoj od jednodušších metod sledování paprsků k inteligentnější, UE asistované správě paprsků.

## Klíčové vlastnosti

- Umožňuje UE zamknout se na konkrétní paprsek gNB pro trvalou komunikaci
- Snižuje režii přepínání paprsků a signalizaci v NR sítích
- Podporuje jak autonomní mechanismy zamknutí paprsku na straně UE, tak síťově řízené
- Integruje se s procedurami měření a hlášení paprsků využívajícími SSB a CSI-RS
- Zlepšuje výkon mobility v milimetrových frekvenčních pásmech (FR2)
- Konfigurovatelné prahové hodnoty a časovače pro uvolnění zámku paprsku a jeho obnovu

## Související pojmy

- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)
- [NR – New Radio](/mobilnisite/slovnik/nr/)

## Definující specifikace

- **TR 38.810** (Rel-16) — NR OTA Test Methods Study
- **TR 38.871** (Rel-18) — Technical Report
- **TR 38.884** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [UBF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ubf/)
