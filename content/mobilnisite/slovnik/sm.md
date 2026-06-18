---
slug: "sm"
url: "/mobilnisite/slovnik/sm/"
type: "slovnik"
title: "SM – MT Short Message Mobile Terminated Point‑to‑Point"
date: 2026-01-01
abbr: "SM"
fullName: "MT Short Message Mobile Terminated Point‑to‑Point"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sm/"
summary: "Služba jádra sítě pro doručování textových zpráv (SMS) ze sítě do mobilního zařízení. Zahrnuje celou sadu protokolů a procedur pro směrování, ukládání a přeposílání zprávy příjemci a tvoří základ služ"
---

SM je služba jádra sítě pro doručování textových zpráv (SMS) ze sítě do mobilního zařízení, zahrnující protokoly a procedury pro jejich směrování, ukládání a přeposílání.

## Popis

[MT](/mobilnisite/slovnik/mt/) Short Message Mobile Terminated Point‑to‑Point (SM-MT) označuje kompletní proces a službu pro doručování zprávy služby [SMS](/mobilnisite/slovnik/sms/) (Short Message Service) ze sítě k mobilní stanici ([MS](/mobilnisite/slovnik/ms/)). Je to jeden ze dvou základních mechanismů přenosu SMS, druhým je Mobile Originated ([MO](/mobilnisite/slovnik/mo/)). Služba je architekturována kolem modelu „ulož a přepošli“ se středobodem v centru služby SMS ([SMSC](/mobilnisite/slovnik/smsc/)). Proces začíná, když SMSC obdrží zprávu určenou pro účastníka. SMSC se dotazuje na domácí registr polohy ([HLR](/mobilnisite/slovnik/hlr/)), aby získal směrovací informace, konkrétně adresu ústředny mobilní sítě/registru polohy návštěvníka ([MSC](/mobilnisite/slovnik/msc/)/[VLR](/mobilnisite/slovnik/vlr/)) nebo uzlu podpory GPRS (SGSN), který účastníka právě obsluhuje. SMSC poté přepošle zprávu tomuto obsluhujícímu uzlu pomocí protokolu MAP (Mobile Application Part) přes signalizaci SS7 nebo na bázi IP.

Po přijetí obsluhující uzel sítě (MSC nebo SGSN) provede několik klíčových funkcí. Nejprve zkontroluje stav účastníka (např. připojen, dosažitelný, neblokován pro SMS). Pokud je zařízení dostupné a v klidovém stavu, uzel zahájí proceduru pagingu, aby jej lokalizoval v rádiové přístupové síti. Následně naváže zabezpečené signalizační spojení (pokud již není přítomno) a doručí zprávu přes řídicí kanál pomocí specifických protokolů: zpráva CP-DATA v rámci podsystému správy spojení (CM) pro doručení přes okruhově spínanou síť prostřednictvím MSC, nebo v rámci správy GPRS relace pro doručení přes paketově spínanou síť prostřednictvím SGSN. Protokolový zásobník zahrnuje vrstvy jako CM, MM (Mobility Management) a vrstvu rádiových zdrojů, které společně zajišťují spolehlivý přenos. Mobilní zařízení potvrdí úspěšné přijetí a toto potvrzení je propagováno zpět k SMSC, který následně označí zprávu jako doručenou. Pokud je zařízení nedostupné, síť použije mechanismy jako příznaky čekající zprávy a plány opakování.

Role SM-MT je klíčová jako doručovací část všudypřítomné služby SMS. Zahrnuje těsnou integraci napříč více doménami sítě: servisní vrstva (SMSC), signalizace jádra sítě (HLR, MSC, SGSN) a rádiová přístupová síť. Její návrh upřednostňuje spolehlivost a efektivitu, využívá řídicí kanály, aby se zabránilo vyčlenění kanálu pro přenos hovoru pro malou datovou zátěž. Služba podporuje jak okruhově spínané, tak paketově spínané metody doručení, přizpůsobuje se připojené doméně účastníka. Tato bezproblémová integrace činí z SMS vysoce spolehlivou, nízkolatenční datovou službu, která funguje paralelně s hlasem a paketovými daty, a tvoří základní komunikační utilitu ve všech generacích sítí 3GPP.

## K čemu slouží

Služba SM-MT byla vytvořena, aby umožnila spolehlivou, síťově iniciovanou schopnost zasílání zpráv, čímž dokončila obousměrný systém SMS. Původní specifikace GSM zahrnovaly SMS jako přidanou službu využívající nevyužitou kapacitu řídicích kanálů. Komponenta Mobile Terminated byla zásadní, aby se SMS stala skutečným interaktivním komunikačním nástrojem, umožňujícím doručení zpráv z jakéhokoli zdroje (jiné mobilní telefony, webové aplikace, operátoři) k účastníkovi.

Historicky, před SMS, nebyla jednoduchá textová komunikace s mobilním zařízením standardizována. Vytvoření procesu SM-MT vyřešilo problém, jak lokalizovat potenciálně pohyblivého příjemce, efektivně doručit malý datový paket bez vyhrazeného hovoru a potvrdit doručení – vše v rámci omezení architektury sítí 2G. Odstranilo to omezení jednosměrných pagingových systémů přidáním potvrzení doručení a integrací se správou identity a mobility účastníka. Model „ulož a přepošli“ SMSC spolu s dotazy na HLR elegantně vyřešil výzvu mobility účastníka, což zajišťuje, že zprávy mohou být doručeny bez ohledu na aktuální polohu uživatele v síti.

Motivace sahala za rámec komunikace mezi osobami. SM-MT se stalo nosičem široké škály služeb: notifikace (upozornění na hlasovou poštu), dvoufaktorové ověřování, příkazy mezi stroji a služby rozhlasových informací. Její spolehlivost a univerzálnost z ní učinily kritický kanál pro komunikaci operátorů s účastníky. Kontinuální vývoj prostřednictvím releasů 3GPP se zaměřil na zvýšení její efektivity, integraci s IP sítěmi, zvýšení bezpečnosti a podporu nových případů užití, jako je SMS přes IMS, a to vše při zachování zpětné kompatibility s miliardami zařízení, která spoléhají na tuto základní službu.

## Klíčové vlastnosti

- Doručování pomocí modelu „ulož a přepošli“ prostřednictvím centra služby SMS (SMSC)
- Integrace s HLR pro směrování účastníka a kontrolu stavu
- Podpora jak okruhově spínaných (prostřednictvím MSC), tak paketově spínaných (prostřednictvím SGSN) mechanismů doručení
- Využívá řídicí kanály pro efektivní přenos bez vyhrazeného kanálu pro přenos hovoru
- Zahrnuje hlášení o doručení a signalizaci potvrzení zpět odesílateli
- Implementuje mechanismy opakování a indikátory čekajících zpráv pro nedostupné účastníky

## Související pojmy

- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [SMSC – Short Message Service Centre](/mobilnisite/slovnik/smsc/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)

## Definující specifikace

- **TS 21.810** (Rel-4) — Multi-mode UE Issues - Categories, principles and procedures
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.910** (Rel-4) — Multi-mode UE Operation Principles
- **TS 22.142** (Rel-19) — Value-added Services for SMS Requirements
- **TR 22.942** (Rel-19) — SMS Value-Added Services Requirements
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TS 23.039** (Rel-5) — SMSC to SME Interface Protocols
- **TS 23.040** (Rel-19) — SMS Technical Realization
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.204** (Rel-19) — SMS over generic IP access; Stage 2
- **TS 23.437** (Rel-20) — SEAL Spatial Map & Anchors
- **TS 23.540** (Rel-19) — 5G Service Based SMS Stage 2
- **TS 23.824** (Rel-10) — IP-SM-GW enhancements for CPM-SMS Interworking
- … a dalších 24 specifikací

---

📖 **Anglický originál a plná specifikace:** [SM na 3GPP Explorer](https://3gpp-explorer.com/glossary/sm/)
