---
slug: "hn"
url: "/mobilnisite/slovnik/hn/"
type: "slovnik"
title: "HN – Home Network"
date: 2025-01-01
abbr: "HN"
fullName: "Home Network"
category: "Core Network"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/hn/"
summary: "Domovská síť (Home Network) je základní infrastruktura mobilního síťového operátora, kde jsou uchovávány trvalé předplatitelské údaje účastníka. Je zodpovědná za autentizaci, autorizaci a účtování pro"
---

HN je základní infrastruktura mobilního síťového operátora, kde jsou uchovávány trvalé předplatitelské údaje účastníka a která zajišťuje autentizaci, autorizaci a účtování.

## Popis

Domovská síť (Home Network, HN) je ústřední architektonický koncept v systémech 3GPP, který představuje mobilního síťového operátora ([MNO](/mobilnisite/slovnik/mno/)), u kterého má účastník trvalé předplatné. Je administrativním a technickým domovem pro profil účastníka, který zahrnuje kritické údaje jako Mezinárodní identifikace mobilního účastníka ([IMSI](/mobilnisite/slovnik/imsi/)), autentizační přihlašovací údaje, profily služeb a informace pro účtování. Fyzická a logická infrastruktura HN zahrnuje základní síťové prvky jako Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), Authentication Centre (AuC) a systémy pro účtování. Jejím hlavním úkolem je spravovat identitu účastníka a vynucovat politiky pro přístup ke službám.

Když se uživatelské zařízení (UE) připojí k síti, obsluhující síť (kterou může být sama HN nebo navštívená síť při roamingu) se musí spojit s HN, aby ověřila identitu účastníka a autorizovala službu. Toho je dosaženo signalizačními protokoly mezi síťovými prvky. Například v LTE a 5G interaguje Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) s HSS v HN. HN autentizuje účastníka pomocí sdílených tajemství uložených v AuC/HSS a poskytuje obsluhující síti profil účastníka, který určuje povolené služby a parametry kvality služby (QoS).

Rozlišení mezi Domovskou sítí (Home Network) a Navštívenou sítí (Visited Network, VN) je klíčové pro umožnění globálního roamingu. HN si zachovává kontrolu nad hlavními daty účastníka a vyrovnává finanční transakce s VN. Z architektonického hlediska HN komunikuje s ostatními sítěmi prostřednictvím mezisíťových dohod a signalizačních systémů, jako je Diameter nebo [HTTP](/mobilnisite/slovnik/http/)/2. V 5G se tento koncept vyvíjí a klíčovou funkcí HN je Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)), který spravuje předplatitelská data a autentizační přihlašovací údaje. Integrita a zabezpečení HN jsou prvořadé, protože je konečnou autoritou pro legitimitu účastníka.

## K čemu slouží

Koncept Domovské sítě existuje proto, aby poskytoval stabilní, centralizovaný kotvný bod pro identitu a správu účastníka v globálně propojeném mobilním ekosystému. Řeší základní problém, jak spolehlivě identifikovat účastníka a autorizovat služby, když se potenciálně může nacházet kdekoli na světě a být připojen prostřednictvím různých přístupových technologií a síťových operátorů. Bez definované Domovské sítě by nebylo možné mobilitu účastníka a roaming spravovat bezpečně a efektivně.

Historicky, jak se buněčné sítě vyvíjely z izolovaných systémů na globální standardy (GSM, UMTS, LTE, 5G), potřeba důvěryhodné domovské autority se stala zřejmou. HN řeší omezení decentralizované správy účastníků tím, že poskytuje jediný zdroj pravdy pro přihlašovací údaje a nároky na služby účastníka. To umožňuje plynulou kontinuitu služeb, konzistentní vynucování politik a centralizované účtování bez ohledu na fyzickou polohu účastníka nebo technologii obsluhující sítě.

Vytvoření a standardizace konceptu HN byly motivovány komerční potřebou roamingu a regulatorními požadavky na identifikaci účastníka. Umožňuje operátorům zachovat si kontrolu nad vztahy se zákazníky a zároveň spolupracovat s jinými sítěmi. HN je základním kamenem architektury roamingu, který umožňuje obchodní a technické modely stojící za moderní globální mobilní komunikací.

## Klíčové vlastnosti

- Ukládá trvalá předplatitelská data a identitu účastníka (např. IMSI)
- Hostí funkce autentizace a autorizace (HSS/AuC/UDM)
- Autorizuje přístup ke službám a vynucuje politiky pro účastníky v domovské síti i při roamingu
- Slouží jako kotvný bod pro záznamy o účtování a tarifikaci
- Poskytuje informace o poloze účastníka autorizovaným síťovým funkcím
- Propojuje se s navštívenými sítěmi prostřednictvím standardizovaných referenčních bodů

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 33.203** (Rel-19) — IMS Security Specification
- **TR 33.741** (Rel-18) — Home Network Triggered Authentication
- **TS 33.822** (Rel-8) — Security Architecture for Inter-Access Mobility
- **TR 33.841** (Rel-16) — Security aspects; Study on 256-bit algorithms for 5G

---

📖 **Anglický originál a plná specifikace:** [HN na 3GPP Explorer](https://3gpp-explorer.com/glossary/hn/)
