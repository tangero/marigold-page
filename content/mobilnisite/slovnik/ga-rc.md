---
slug: "ga-rc"
url: "/mobilnisite/slovnik/ga-rc/"
type: "slovnik"
title: "GA-RC – Generic Access - Resource Control"
date: 2025-01-01
abbr: "GA-RC"
fullName: "Generic Access - Resource Control"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ga-rc/"
summary: "Protokol v rámci architektury Generic Access Network (GAN), známé také jako UMA, pro správu zdrojů a řízení spojení mezi mobilním zařízením a GAN Controllerem (GANC) přes neregulované bezdrátové IP sí"
---

GA-RC je protokol v rámci architektury Generic Access Network pro správu zdrojů a řízení spojení mezi mobilním zařízením a GANC přes neregulované IP sítě, který umožňuje plynulé předávání spojení mezi buněčným a IP přístupem.

## Popis

GA-RC (Generic Access - Resource Control) je klíčový řídicí protokol specifikovaný ve standardech 3GPP Generic Access Network ([GAN](/mobilnisite/slovnik/gan/)), které definují technologii Unlicensed Mobile Access (UMA). Funguje mezi mobilním zařízením, označovaným jako Generic Access - Mobile Station (GA-MS), a síťovou entitou známou jako Generic Access Network Controller ([GANC](/mobilnisite/slovnik/ganc/)). Primární funkcí GA-RC je řídit vytvoření, udržování a uvolnění zabezpečeného logického řídicího spojení přes neregulovanou bezdrátovou IP přenosovou síť, typicky Wi-Fi nebo Bluetooth. Toto spojení, známé jako signalizační spojení GA-RC, je předpokladem pro všechny ostatní procedury GAN včetně registrace, autentizace a nastavování přenosových cest pro přepojované okruhy ([CS](/mobilnisite/slovnik/cs/)) i přepojované pakety (PS).

Architektonicky se GA-RC nachází v GA-MS a GANC nad podkladovou IP transportní vrstvou. Je zodpovědný za proceduru navázání spojení GA-RC, která zahrnuje to, že mobilní zařízení objeví GANC, naváže TCP spojení na definovaný port a následně provede vzájemnou autentizaci a nastavení zabezpečení pomocí procedury GA-RC SECURITY MODE CONTROL. Tím je zajištěna integrita a důvěrnost všech následných signalizačních zpráv. Jakmile je zabezpečené spojení GA-RC aktivní, může se mobilní zařízení prostřednictvím GANC zaregistrovat v jádru sítě, a vypadat tak, jako by bylo připojeno přes standardní buněčnou přístupovou síť (např. [GERAN](/mobilnisite/slovnik/geran/)). GANC slouží jako překladový bod, který převádí zprávy GA-RC na ekvivalentní zprávy [BSSAP](/mobilnisite/slovnik/bssap/) (pro CS) nebo RANAP (pro PS) pro jádro sítě.

Protokol definuje komplexní stavový automat a sadu zpráv pro správu spojení, zpracování chyb a mechanizmy keep-alive. Mezi klíčové procedury patří GA-RC REGISTER pro počáteční připojení, GA-RC DEREGISTER pro odpojení a GA-RC REGISTER UPDATE pro aktualizace mobility. Protokol také řeší přesměrování na alternativní GANC pro vyrovnávání zátěže nebo obnovu. GA-RC funguje ve spolupráci s dalšími protokoly GAN: [GA-CSR](/mobilnisite/slovnik/ga-csr/) (pro hlas/SMS s přepojováním okruhů) a [GA-PSR](/mobilnisite/slovnik/ga-psr/) (pro datové přenosy s přepojováním paketů) jsou závislé na zabezpečeném tunelu zřízeném GA-RC. Jeho role je základní, neboť poskytuje řízený a zabezpečený 'kanál', jímž proudí veškerý další služebně specifický signalizační a uživatelský provoz, což umožňuje dvoumodemovým terminálům používat IP přístup jako funkční alternativu k tradiční buněčné radiové síti.

## K čemu slouží

GA-RC byl vytvořen jako součást specifikací 3GPP Generic Access Network ([GAN](/mobilnisite/slovnik/gan/)), zavedených ve vydání 6 a formálně standardizovaných ve vydání 8, aby řešil rostoucí potřebu konvergence pevných a mobilních sítí (FMC). Primární problém, který řešil, bylo omezené vnitřní pokrytí buněčných sítí, zejména pro hlasové služby. Využitím všudypřítomných technologií využívajících neregulované spektrum, jako je Wi-Fi, mohli operátoři rozšířit dosah svých služeb do domácností, kanceláří a hotspotů, zlepšit zkušenost zákazníků a snížit odliv zákazníků. GA-RC poskytl nezbytný řídicí mechanismus pro zabezpečenou a spolehlivou integraci těchto různorodých IP přístupových sítí do důvěryhodného mobilního jádra.

Historicky, před GAN, byla řešení pro využití Wi-Fi pro mobilní služby proprietární nebo omezená pouze na datové VoIP aplikace a postrádala plynulou integraci s klíčovými mobilními funkcemi, jako je předávání spojení, konzistentní identita účastníka a plná kontinuita služeb. GA-RC, jakožto protokol pro řízení zdrojů, byl motivován potřebou standardizované metody na úrovni operátora pro autentizaci zařízení, vytváření zabezpečených tunelů a správu stavu logického spojení. Řešil omezení ad-hoc IP připojení poskytnutím formalizovaného procesu registrace a správy relací, což zajistilo, že zařízení připojené přes Wi-Fi může být spravováno se stejnou úrovní zabezpečení a řízení pravidel jako zařízení připojené přes buněčnou základnovou stanici. Toto umožnilo realizaci vize 'UMA', kde se přístupová síť stala transparentní pro služby jádra.

## Klíčové vlastnosti

- Vytváří a spravuje zabezpečené řídicí spojení mezi GA-MS a GANC
- Provádí vzájemnou autentizaci a nastavení režimu zabezpečení pro integritu a důvěrnost signalizace
- Zpracovává procedury objevení GANC, registrace, odregistrování a aktualizace registrace
- Řídí chybové stavy a poskytuje schopnost přesměrování na alternativní GANC
- Definuje stavový automat pro spolehlivou správu životního cyklu spojení
- Poskytuje základní řídicí kanál pro služební protokoly GA-CSR a GA-PSR

## Související pojmy

- [GANC – Generic Access Network Controller](/mobilnisite/slovnik/ganc/)
- [GA-CSR – Generic Access - Circuit Switched Resources](/mobilnisite/slovnik/ga-csr/)
- [GA-PSR – Generic Access - Packet Switched Resources](/mobilnisite/slovnik/ga-psr/)

## Definující specifikace

- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [GA-RC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ga-rc/)
