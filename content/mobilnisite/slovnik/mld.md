---
slug: "mld"
url: "/mobilnisite/slovnik/mld/"
type: "slovnik"
title: "MLD – Multicast Listener Discovery"
date: 2025-01-01
abbr: "MLD"
fullName: "Multicast Listener Discovery"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mld/"
summary: "Protokol umožňující IPv6 směrovačům objevovat multicastové posluchače na přímo připojených linkách. Je nezbytný pro efektivní správu IP multicastových skupin, protože umožňuje směrovačům zjistit, kter"
---

MLD je protokol, který umožňuje IPv6 směrovačům zjistit, které přímo připojené uzly si přejí přijímat multicastový provoz, což umožňuje efektivní správu multicastových skupin a optimalizaci síťových zdrojů.

## Popis

Multicast Listener Discovery (MLD) je součástí sady protokolů IPv6, odvozená od protokolu Internet Group Management Protocol ([IGMP](/mobilnisite/slovnik/igmp/)) pro IPv4. Funguje mezi IPv6 směrovačem a hostiteli na jeho přímo připojených linkách. Hlavní funkcí MLD je umožnit směrovači zjistit přítomnost multicastových posluchačů – hostitelů, kteří si přejí přijímat pakety určené pro konkrétní IPv6 multicastové adresy – a určit, které multicastové adresy jsou zajímavé pro každou z jeho připojených linek. Tento proces zjišťování je klíčový pro vytvoření potřebného stavu pro efektivní směrování multicastového provozu, což zajišťuje, že pakety jsou odesílány pouze na linky, kde jsou zájemci o příjem.

MLD funguje prostřednictvím výměny dotazovacích a hláš[ec](/mobilnisite/slovnik/ece-c/)ích zpráv. Směrovač, který vystupuje jako multicastový dotazovatel, periodicky odesílá obecné dotazy (General Query) na linkově lokální multicastovou adresu všech uzlů (FF02::1), aby vyžádal informace o členství. Hostitelé odpovídají odesláním zpráv Multicast Listener Report pro každou multicastovou skupinu, kterou si přejí připojit, čímž vyjádří svůj zájem dotazovateli. Když hostitel opouští skupinu, může odeslat zprávu Multicast Listener Done (v MLDv1) nebo specifické hlášení (v MLDv2), aby informoval směrovač. Směrovač udržuje časovač pro každou multicastovou skupinu na každém rozhraní; pokud není před vypršením časovače přijato žádné hlášení, směrovač předpokládá, že na lince nejsou žádní posluchači, a přestane na ni přeposílat provoz pro danou skupinu.

Protokol existuje ve dvou verzích: MLDv1 (specifikovaná v RFC 2710) a MLDv2 (specifikovaná v RFC 3810). MLDv1 poskytuje základní funkcionalitu analogickou IGMPv2, podporuje hlášení o členství ve skupině a opuštění skupiny. MLDv2 zavádí filtrování podle zdroje, což umožňuje hostitelům hlásit zájem o příjem provozu pouze od konkrétních zdrojových adres (režim INCLUDE) nebo od všech zdrojů kromě konkrétních (režim EXCLUDE). To poskytuje podporu pro Source-Specific Multicast (SSM). V rámci architektur 3GPP je MLD relevantní pro IP služby, zejména v kontextu IP Multimedia Subsystem (IMS) a doručování multicastových služeb přes mobilní sítě, kde je efektivní správa skupin klíčová pro služby jako mobilní TV nebo skupinová komunikace.

## K čemu slouží

MLD byl vytvořen, aby řešil potřebu efektivní správy multicastových skupin v sítích IPv6. S rozšiřováním nasazení IPv6 se staly zřejmými omezení používání protokolů zaměřených na IPv4, jako je [IGMP](/mobilnisite/slovnik/igmp/), což si vyžádalo nativní řešení pro IPv6. Multicast je metoda efektivního využití šířky pásma pro doručování stejného obsahu více příjemcům, ale vyžaduje mechanismus, který umožní směrovačům dynamicky zjišťovat, kteří hostitelé mají zájem o které multicastové skupiny na každém síťovém segmentu. Bez takového mechanismu by směrovače buď zaplavovaly multicastový provoz na všechny linky (plýtvání šířkou pásma), nebo by vyžadovaly statickou konfiguraci (která je nepružná a neškálovatelná).

MLD řeší problém dynamického zjišťování multicastových posluchačů a umožňuje tak sémantiku 'přihlásit se a přijímat' pro IP multicast. To je základní pro škálovatelné služby komunikace jeden–k–mnoha a mnoho–k–mnoha. V kontextu sítí 3GPP přijetí plně IP architektur, zejména se zavedením IP Multimedia Subsystem (IMS) ve verzi 5, učinilo efektivní správu IP multicastu kritickým požadavkem pro doručování multimediálních vysílacích/multicastových služeb ([MBMS](/mobilnisite/slovnik/mbms/)) a dalších skupinových aplikací přes mobilní přenosové sítě. MLD poskytuje standardizovaný mechanismus na úrovni protokolu, který to umožňuje.

## Klíčové vlastnosti

- Dynamické zjišťování IPv6 multicastových posluchačů na síťové lince
- Výměna dotazovacích, hlášecích a dokončovacích zpráv mezi směrovači a hostiteli
- Podpora modelů any-source multicast (ASM) i source-specific multicast (SSM) v MLDv2
- Schopnost filtrování podle zdroje, která umožňuje hostitelům specifikovat požadované zdrojové adresy
- Správa stavu multicastového naslouchání na straně směrovače s využitím časovačů
- Fungování protokolu nezávislé na multicastovém směrovacím protokolu používaném v jádru sítě

## Související pojmy

- [IGMP – Internet Group Management Protocol](/mobilnisite/slovnik/igmp/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.316** (Rel-19) — Wireline and Wireless Convergence Access Support
- **TS 23.846** (Rel-6) — MBMS Architecture and Functionality
- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN

---

📖 **Anglický originál a plná specifikace:** [MLD na 3GPP Explorer](https://3gpp-explorer.com/glossary/mld/)
