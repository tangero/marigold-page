---
slug: "mcch"
url: "/mobilnisite/slovnik/mcch/"
type: "slovnik"
title: "MCCH – MBMS point-to-multipoint Control Channel"
date: 2025-01-01
abbr: "MCCH"
fullName: "MBMS point-to-multipoint Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mcch/"
summary: "Logický kanál v sítích 3GPP používaný výhradně pro vysílání řídicích informací souvisejících se službou Multimedia Broadcast Multicast Services (MBMS). Přenáší klíčové konfigurační a plánovací údaje p"
---

MCCH je logický kanál v sítích 3GPP, který vysílá řídicí informace MBMS, včetně konfiguračních a plánovacích údajů pro kanály MTCH, aby umožnil doručování obsahu bod–více bodů.

## Popis

Řídicí kanál [MBMS](/mobilnisite/slovnik/mbms/) bod–více bodů (MCCH) je downlinkový logický kanál definovaný v architektuři rádiového přístupového sítě 3GPP. Funguje jako klíčová součást rámce MBMS, který je navržen pro efektivní poskytování vysílacích a skupinových služeb. Jako logický kanál je MCCH mapován na transportní kanály a nakonec na fyzické kanály pro přenos přes rozhraní vzduchu. Jeho primární funkcí je přenášet informace řídicí roviny nezbytné pro to, aby uživatelská zařízení (UE) mohla přijímat služby MBMS na skupinovém datovém kanálu ([MTCH](/mobilnisite/slovnik/mtch/)). Tyto informace zahrnují oznámení služeb MBMS, upozornění na začátek relace a především konfigurační zprávy řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)), které určují, jak je přidružený MTCH plánován a vysílán. MCCH je vysílán způsobem bod–více bodů v rámci oblasti MBMS Single Frequency Network ([MBSFN](/mobilnisite/slovnik/mbsfn/)), což znamená, že jediný přenos přijímají všechna přihlášená uživatelská zařízení (UE) v dané geografické zóně.

Z architektonického hlediska je MCCH definován pro každou oblast MBSFN. Oblast MBSFN je skupina buněk, které jsou synchronizovány pro vysílání identických vlnových tvarů pro obsah MBMS, čímž vytvářejí souvislý vysílací region. V rámci každé oblasti MBSFN existuje jeden jedinečný MCCH. Síť používá bloky systémových informací ([SIB](/mobilnisite/slovnik/sib/)), konkrétně SIB13 v LTE a SIB20 v NR, aby informovala uživatelská zařízení (UE) o plánování a konfiguraci samotného MCCH. To zahrnuje parametry jako modifikační perioda, perioda opakování a přidělení dílčích rámců. Uživatelské zařízení (UE) po získání tohoto SIB ví, kdy a kde má naslouchat MCCH, aby získalo potřebnou konfiguraci RRC (zprávu MBSFNAreaConfiguration) pro MTCH, o které má zájem.

Provoz MCCH je charakterizován jeho periodickým mechanismem a mechanismem upozorňování na změny. Je vysílán v předem definovaných intervalech. Pro úsporu baterie uživatelského zařízení (UE) je použit mechanismus upozornění na změnu. Krátká upozornění jsou odesílána na souvisejícím fyzickém kanálu (např. [MICH](/mobilnisite/slovnik/mich/) v UMTS, [PDCCH](/mobilnisite/slovnik/pdcch/) s [G-RNTI](/mobilnisite/slovnik/g-rnti/)/MCS-RNTI v LTE/NR), aby upozornila uživatelská zařízení (UE) pouze tehdy, když se informace MCCH chystá změnit v následující modifikační periodě. Pokud není detekováno žádné upozornění, může uživatelské zařízení (UE) předpokládat, že předchozí konfigurace MCCH zůstává platná, a nemusí MCCH opakovaně dekódovat. Obsah MCCH zahrnuje seznam služeb MBMS (identifikovaných pomocí dočasných identifikátorů mobilní skupiny – TMGI) aktivních v oblasti a pro každou z nich přidruženou konfiguraci logického kanálu pro MTCH. To uživatelskému zařízení (UE) sděluje konkrétní konfiguraci rádiového přenosu, plánování a MCS (schéma modulace a kódování), které má použít pro dekódování multimediálního obsahu.

V celkové protokolové zásobníku existuje MCCH na vrstvě RRC. Informace jsou generovány entitou RRC v základnové stanici (eNodeB/gNB) na základě pokynů z koordinační entity MBMS v jádru sítě (MCE). Poté jsou předány dolů přes vrstvy Packet Data Convergence Protocol (PDCP), Radio Link Control (RLC) a Medium Access Control (MAC), kde jsou jim přiděleny specifické transportní a fyzické prostředky. Jeho role je pro MBMS zásadní, protože bez řídicích informací, které poskytuje, by uživatelská zařízení (UE) nebyla schopna objevit, synchronizovat se a správně dekódovat vysílané multimediální proudy, což by znemožnilo poskytování služeb bod–více bodů.

## K čemu slouží

MCCH byl vytvořen, aby vyřešil zásadní problém signalizace řízení pro vysílací/skupinové služby v celulárních sítích. Tradiční jednosměrné služby používají vyhrazené signalizační kanály pro každé uživatelské zařízení (UE), což je pro služby doručující identický obsah tisícům zařízení, jako je mobilní TV nebo streamování živých událostí, velmi neefektivní. Bez sdíleného řídicího kanálu by síť musela odesílat jednotlivé konfigurační zprávy RRC každému uživatelskému zařízení (UE), což by spotřebovávalo nadměrné množství downlinkových rádiových prostředků a signalizační kapacity jádra sítě.

Zavedení MBMS ve verzi 3GPP Release 6 si vyžádalo doplňkový řídicí mechanismus, který by odpovídal efektivitě datového kanálu bod–více bodů (MTCH). MCCH toto poskytuje tím, že řídicí informace vysílá jednou pro všechna uživatelská zařízení (UE) v oblasti. Tento návrh je vnitřně spojen s konceptem provozu MBSFN, kde více buněk vysílá synchronně. MCCH nese jednotnou konfiguraci, která umožňuje všem uživatelským zařízením (UE) správně se naladit na tento synchronizovaný přenos. Jeho účel přesahuje pouhou efektivitu; umožňuje škálovatelnost služeb, což dovoluje neomezenému počtu uživatelských zařízení (UE) připojit se k vysílací relaci bez dopadu na zatížení řídicího kanálu. Také usnadňuje základní funkce MBMS, jako je oznamování služeb (informování uživatelských zařízení o dostupných vysíláních) a řízení relací (signalizace začátku a konce vysílacího proudu).

Historicky, před vyhrazenými vysílacími systémy jako MBMS, vyžadovalo doručování populárního obsahu masivní duplikaci jednosměrných přenosů, což mohlo zahlcovat síť. MCCH jako součást architektury MBMS poskytl standardizovanou, s celulární sítí integrovanou řídicí rovinu, která učinila síťové vysílání životaschopnou a efektivní službou pro operátory. Odstranil omezení předchozích necelaulárních vysílacích technologií (jako DVB-H) tím, že umožnil těsnou integraci s celulárním řízením mobility a obousměrnými schopnostmi, přičemž MCCH sloužil jako jednosměrný vysílací kanál pro všechny potřebné parametry příjmu.

## Klíčové vlastnosti

- Vysílá řídicí informace MBMS bod–více bodů v rámci oblasti MBSFN.
- Přenáší konfigurační zprávy RRC (MBSFNAreaConfiguration) pro dekódování MTCH.
- Využívá mechanismus upozornění na změnu (např. přes PDCCH) pro minimalizaci spotřeby energie uživatelského zařízení (UE).
- Konfigurován a plánován pomocí systémových informací (SIB13 v LTE, SIB20 v NR).
- Vysílán periodicky s definovanými modifikačními a opakovacími periodami.
- Obsahuje seznam aktivních služeb MBMS a jejich přidružené konfigurace rádiového přenosu.

## Související pojmy

- [MTCH – MBMS point-to-multipoint Traffic Channel](/mobilnisite/slovnik/mtch/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)
- [MCE – Multi-cell/multicast Coordination Entity](/mobilnisite/slovnik/mce/)
- [MBS – Frequency Selection Area Identity](/mobilnisite/slovnik/mbs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.468** (Rel-19) — Group Communication System Enablers for LTE
- **TS 23.479** (Rel-19) — MBMS API for Mission Critical Services
- **TS 23.792** (Rel-16) — MBMS API for Mission Critical Services
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.346** (Rel-19) — MBMS in UTRA Technical Specification
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- … a dalších 13 specifikací

---

📖 **Anglický originál a plná specifikace:** [MCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/mcch/)
