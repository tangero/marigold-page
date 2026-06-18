---
slug: "rau"
url: "/mobilnisite/slovnik/rau/"
type: "slovnik"
title: "RAU – Routeing Area Update"
date: 2025-01-01
abbr: "RAU"
fullName: "Routeing Area Update"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rau/"
summary: "Procedura v GPRS/UMTS, při kterém mobilní zařízení aktualizuje síť o své aktuální poloze v směrovací oblasti (RA). Umožňuje efektivní mobilitu v paketově orientované části sítě (packet-switched), což"
---

RAU je procedura mobility v GPRS/UMTS, při kterém mobilní zařízení aktualizuje síť o své aktuální směrovací oblasti (Routeing Area) pro efektivní vyvolávání (paging) a směrování dat.

## Popis

Routeing Area Update (RAU) je základní procedura správy mobility definovaná v paketově orientované ([PS](/mobilnisite/slovnik/ps/)) části 3GPP sítí, primárně pro [GPRS](/mobilnisite/slovnik/gprs/) a UMTS. Funguje v kontextu protokolu GPRS Mobility Management ([GMM](/mobilnisite/slovnik/gmm/)). Směrovací oblast ([RA](/mobilnisite/slovnik/ra/)) je logická oblast, typicky zahrnující jednu nebo více lokalizačních oblastí ([LA](/mobilnisite/slovnik/la/)) používaných pro služby s přepojováním okruhů (circuit-switched), definovaná pro sledování polohy uživatelského zařízení (UE) pro datové služby. Základním síťovým elementem zodpovědným za PS mobilitu je Serving GPRS Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)). Procedura RAU je iniciována, když UE detekuje, že vstoupilo do nové RA, na základě identifikátoru RA ([RAI](/mobilnisite/slovnik/rai/)) vysílaného síťovými buňkami. Je také iniciována periodicky podle timeru (periodic RAU) nebo při zapnutí UE (RAU after power-on).

Procedura zahrnuje vyslání zprávy RAU REQUEST od UE k novému SGSN (pokud je RAU mezi různými SGSN, inter-SGSN RAU) nebo ke svému aktuálnímu SGSN (pokud je RAU uvnitř stejného SGSN, intra-SGSN RAU). Tato zpráva obsahuje identitu UE (např. [P-TMSI](/mobilnisite/slovnik/p-tmsi/)) a jeho předchozí polohovou informaci. V inter-SGSN RAU nový SGSN použije tuto informaci ke kontaktování starého SGSN pro získání MM a PDP kontextů UE, což zajistí kontinuitu session. Nový SGSN pak autentizuje UE a aktualizuje polohu UE v Home Location Register (HLR), který následně zruší registraci na starém SGSN. SGSN pak odpoví zprávou RAU ACCEPT, přidělí nové Packet-Temporary Mobile Subscriber Identity (P-TMSI) pokud je to nutné.

RAU je klíčová pro udržování přesné polohy UE v PS části sítě bez nutnosti konstantní signalizace. Umožňuje síti efektivně vyvolat UE pro příchozí datové pakety pouze v jeho poslední známé RA, namísto v celé síti. Tím se snižuje provoz vyvolávání (paging traffic) a šetří se rádiové prostředky. Navíc, díky seskupení buněk do RA, síť vyvažuje náklady signalizace aktualizace polohy proti nákladům vyvolávání. Procedura funguje spolu s dalšími stavy jako IDLE, STANDBY a READY, definující kdy jsou aktualizace polohy potřebné. Její úspěšné dokončení zajistí, že Gateway GPRS Support Node (GGSN) má správnou adresu SGSN pro tunelování datových paketů uživatele k aktuálně obsluhujícímu nodu UE.

## K čemu slouží

RAU byl vytvořen pro řešení potřeb efektivní správy mobility v paketově orientovaných (packet-switched) mobilních sítích, konkrétně GPRS a UMTS. Před GPRS byla mobilita primárně navržena pro hlasové služby s přepojováním okruhů (circuit-switched), používající aktualizace lokalizační oblasti (LAU). Datové služby však mají odlišné charakteristiky provozu – často bursty a intermitentní – což vyžaduje schéma správy mobility optimalizované pro data. Primární problém, který RAU řeší, je umožnění síti znát přibližnou polohu UE pro doručení downlink paketů bez nutnosti, aby UE bylo konstantně aktivní na rádiu, což by vyčerpalo jeho baterii.

Bez RAU by síť buď ztratila přehled o poloze UE, což by způsobilo ztrátu datových session při pohybu, nebo by musela vyvolávat UE v neprakticky velké oblasti pro každý příchozí datový paket, což by spotřebovávalo nadměrné rádiové pásmo a signalizační prostředky. RAU zavádí koncept směrovací oblasti (RA), která může být větší než lokalizační oblast (LA), pro snížení frekvence aktualizací v porovnání s LAU pro datově orientované zařízení. Tento design reflektuje, že datové session mohou tolerovat méně přesnou polohovou informaci než hlasové hovory, vyvažuje určitou granularitu lokalizace za významné zvýšení signalizační efektivity a úspory energie UE. RAU tvoří základ 'always-on' připojení pro mobilní data, umožňující UE být dostupné pro IP provoz, zatímco většinu času je ve stavu s nízkou spotřebou energie a šetřícím rádiové prostředky.

## Klíčové vlastnosti

- Iniciuje při překročení hranice směrovací oblasti (RA)
- Podporuje aktualizace uvnitř SGSN (intra-SGSN) i mezi SGSN (inter-SGSN)
- Obsahuje periodické mechanismy aktualizace a aktualizaci při zapnutí
- Umožňuje transfer kontextů mezi SGSN pro kontinuitu session
- Integruje autentizační a bezpečnostní procedury (např. přeadělování P-TMSI)
- Umožňuje efektivní vyvolávání (paging) v síti v poslední známé RA

## Související pojmy

- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [P-TMSI – Packet-Temporary Mobile Subscriber Identity](/mobilnisite/slovnik/p-tmsi/)
- [GMM – Global Multimedia Mobility](/mobilnisite/slovnik/gmm/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.859** (Rel-11) — UTRAN Key Hierarchy Enhancement Study
- **TS 36.878** (Rel-13) — LTE Performance Enhancements for High Speed Scenarios
- **TS 43.129** (Rel-19) — PS Handover in GERAN A/Gb and GAN Modes
- **TS 45.820** (Rel-13) — CIoT for Internet of Things

---

📖 **Anglický originál a plná specifikace:** [RAU na 3GPP Explorer](https://3gpp-explorer.com/glossary/rau/)
