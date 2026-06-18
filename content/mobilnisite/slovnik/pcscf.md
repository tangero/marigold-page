---
slug: "pcscf"
url: "/mobilnisite/slovnik/pcscf/"
type: "slovnik"
title: "PCSCF – Proxy Call Session Control Function"
date: 2025-01-01
abbr: "PCSCF"
fullName: "Proxy Call Session Control Function"
category: "Core Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/pcscf/"
summary: "PCSCF je prvním kontaktním bodem pro uživatelské zařízení (UE) v IP multimediální podsystému (IMS). Funguje jako proxy server pro protokol SIP (Session Initiation Protocol), zajišťuje řízení relací, z"
---

PCSCF je první kontaktní bod SIP proxy pro uživatelské zařízení (User Equipment) v IMS, který zajišťuje řízení relací, zabezpečení a vynucování pravidel pro navazování multimediálních relací, jako je VoLTE, přes paketovou doménu.

## Popis

Proxy Call Session Control Function (PCSCF) je základní uzel v architektuře IP multimediálního podsystému (IMS) definované 3GPP. Slouží jako vstupní bod pro veškerou signalizaci [SIP](/mobilnisite/slovnik/sip/) z uživatelského zařízení (UE) do sítě IMS. Když UE zahájí relaci, například hlasové nebo videohovory, odesílá zprávy SIP na PCSCF, který objeví pomocí [DHCP](/mobilnisite/slovnik/dhcp/) nebo jiných mechanismů. Primární úlohou PCSCF je fungovat jako proxy server SIP, který tyto zprávy přeposílá příslušným prvkům jádra IMS, jako je Interrogating-CSCF ([I-CSCF](/mobilnisite/slovnik/i-cscf/)) nebo Serving-CSCF ([S-CSCF](/mobilnisite/slovnik/s-cscf/)), na základě cíle relace a servisní logiky. Sám nerozhoduje o směrování na základě servisní logiky, ale zajišťuje, že signalizace dorazí k síťovým prvkům, které to dělají.

Kromě základního proxy funkce je PCSCF zodpovědný za několik klíčových bezpečnostních a politických funkcí. Vytváří a udržuje bezpečnostní asociace [IPsec](/mobilnisite/slovnik/ipsec/) ([SA](/mobilnisite/slovnik/sa/)) s UE, aby zajistil integritu a důvěrnost signalizace SIP. To je klíčová součást procedury IMS Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)). PCSCF také vynucuje lokální politiku, například ověřuje, zda je UE autorizováno používat pro relaci určité typy médií nebo kodeky. Interaguje s funkcí Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) přes rozhraní Rx, aby aplikoval dynamickou politiku kvality služeb (QoS) a účtování na přenosovou vrstvu, čímž zajišťuje, že přenosová síť poskytne potřebné prostředky pro relaci IMS.

Z architektonického hlediska může být PCSCF nasazen v domovské síti nebo, častěji v roamovacích scénářích, v navštívené síti. Když je v navštívené síti, je znám jako P-CSCF a přeposílá signalizaci do domovské sítě na I-CSCF. Také provádí funkce jako komprese zpráv SIP (SigComp) pro optimalizaci signalizace přes rádiová spojení s omezenou šířkou pásma a podporuje zpracování nouzových relací. PCSCF je pro samotnou relaci bezstavový; neudržuje stav relace, ale může udržovat stav související s bezpečnostními asociacemi. Jeho fungování je definováno v mnoha specifikacích 3GPP, včetně TS 24.229 pro signalizaci SIP a uvedených specifikací pro správu, což zajišťuje interoperabilitu a konzistentní chování napříč síťovými nasazeními.

## K čemu slouží

PCSCF byl zaveden, aby umožnil poskytování IP služeb založených na multimédiích přes mobilní sítě, což je hlavním cílem architektury IMS standardizované od 3GPP Release 5. Před IMS řešily hlas a základní služby sítě s přepojováním okruhů, které však nebyly vhodné pro flexibilní, IP založené multimediální aplikace plánované pro budoucí sítě. PCSCF řeší problém bezpečného a efektivního připojení mobilních UE ke službové vrstvě plně založené na IP, odděluje poskytování služeb od podkladové přístupové technologie (např. GPRS, LTE, 5G NR).

Jeho vytvoření bylo motivováno potřebou standardizovaného, bezpečného vstupního bodu, který by dokázal zvládnout složitosti signalizace SIP v mobilním prostředí. To zahrnuje správu mobility uživatelů, vynucování síťových politik a zajištění, aby QoS pro služby v reálném čase, jako je hlas, mohla být garantována přes paketový přenos. Tím, že funguje jako důvěryhodný proxy server, PCSCF chrání jádro sítě IMS před přímou expozicí UE a poskytuje vrstvu zabezpečení a kontroly. Také umožňuje nezbytné funkce pro komerční nasazení, jako je integrace s řízením politik pro správu zdrojů a účtování, což nebylo problémem v tradičních internetových nasazeních SIP.

## Klíčové vlastnosti

- Funkce SIP proxy: Slouží jako první kontaktní bod a proxy pro veškerou signalizaci SIP mezi UE a jádrem IMS.
- Bezpečnostní brána: Vytváří a udržuje bezpečnostní asociace IPsec s UE pro ochranu integrity a důvěrnosti signalizace SIP.
- Vynucování pravidel: Interaguje s PCRF přes rozhraní Rx, aby aplikoval pravidla QoS a účtování na přenosovou síť.
- Komprese zpráv SIP: Podporuje SigComp pro snížení režie signalizace přes rádiové rozhraní.
- Podpora nouzových relací: Identifikuje a správně směruje nouzové hovory, a to i když není UE plně registrováno.
- Podpora roamingu: Může být nasazen v navštívené síti pro zpracování místního breakoutu a optimalizaci signalizačních cest pro roamující uživatele.

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)
- [I-CSCF – Interrogating-Call Session Control Function](/mobilnisite/slovnik/i-cscf/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 32.632** (Rel-11) — Core Network Resources IRP: Network Resource Model
- **TS 32.732** (Rel-11) — IMS Network Resource Model IRP: Information Service

---

📖 **Anglický originál a plná specifikace:** [PCSCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/pcscf/)
