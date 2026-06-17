---
slug: "apn-oi"
url: "/mobilnisite/slovnik/apn-oi/"
type: "slovnik"
title: "APN-OI – Access Point Name Operator Identifier"
date: 2025-01-01
abbr: "APN-OI"
fullName: "Access Point Name Operator Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/apn-oi/"
summary: "APN-OI je součástí názvu přístupového bodu (APN) používaného v sítích 3GPP k jednoznačné identifikaci domény operátora. Je klíčový pro směrování datového provozu uživatele ke správné bráně paketové da"
---

APN-OI je součástí názvu přístupového bodu (Access Point Name), která jednoznačně identifikuje doménu operátora pro směrování datového provozu ke správné bráně paketové datové sítě (Packet Data Network Gateway) a podporuje roamování.

## Popis

Identifikátor operátora v názvu přístupového bodu (Access Point Name Operator Identifier, APN-OI) je kritická dílčí součást v rámci celé struktury názvu přístupového bodu ([APN](/mobilnisite/slovnik/apn/)) používaného pro paketovou datovou konektivitu v sítích 3GPP, jako je EPS (Evolved Packet System) a 5GS. APN je plně kvalifikovaný doménový název ([FQDN](/mobilnisite/slovnik/fqdn/)), který identifikuje konkrétní paketovou datovou síť (PDN), ke které si uživatelské zařízení (UE) přeje připojit, například internet nebo síť IMS. APN-OI konkrétně tvoří část tohoto FQDN příslušející doméně operátora. Typicky se skládá z mobilního síťového kódu ([MNC](/mobilnisite/slovnik/mnc/)) a mobilního kódu země ([MCC](/mobilnisite/slovnik/mcc/)), po kterých následuje přípona domény operátora (např. '.gprs'), čímž vzniká struktura jako 'mnc<MNC>.mcc<MCC>.gprs'. Tento standardizovaný formát zajišťuje globální jedinečnost.

Z architektonického hlediska hraje APN-OI klíčovou roli během procedury navazování spojení k PDN, primárně v EPS. Když UE iniciuje žádost o spojení k PDN, může poskytnout APN nebo mu jej síť přidělí. Síťové prvky, zejména [MME](/mobilnisite/slovnik/mme/) (Mobility Management Entity) a SGW (Serving Gateway), používají APN-OI k určení cílové brány paketové datové sítě (PGW). PGW je síťový uzel, který funguje jako rozhraní mezi sítí 3GPP a externí PDN. APN-OI pomáhá při výběru PGW tím, že identifikuje doménu sítě operátora, ve které se PGW nachází, což je zásadní jak pro provoz směrovaný přes domovskou síť (home-routed), tak pro scénáře místního průniku (local breakout) v navštívených sítích.

Ve scénářích roamování nabývá APN-OI ještě většího významu. Pro UE roamující v navštívené veřejné pozemní mobilní síti (VPLMN) obsahuje APN poskytnutý UE nebo domovskou sítí APN-OI domovské veřejné pozemní mobilní sítě ([HPLMN](/mobilnisite/slovnik/hplmn/)). Síťové uzly VPLMN tento APN-OI analyzují. Na základě roamingových dohod a konfigurace se mohou rozhodnout, zda datový provoz směrovat na PGW v HPLMN (home-routed traffic), nebo zvolit PGW ve VPLMN (local breakout). Toto rozhodnutí ovlivňuje datovou cestu, latenci a účtování. APN-OI je tedy základním směrovacím identifikátorem, který podporuje globální interoperabilitu mobilních datových služeb.

APN-OI je definován a přenášen v rámci protokolů 3GPP, nejvýznamněji v [GTP](/mobilnisite/slovnik/gtp/) ([GPRS](/mobilnisite/slovnik/gprs/) Tunnelling Protocol) používaném mezi SGW a PGW a v signalizaci S1-AP a NAS (Non-Access Stratum). Jeho konzistentní interpretaci napříč různými síťovými prvky a operátory zajišťují specifikace 3GPP. Zatímco základní koncept zůstává, jeho použití a kontext se vyvinuly se zavedením 5G systému (5GS), kde je analogickým konceptem název datové sítě (DNN) a výběr funkce správy relací (SMF) a funkce uživatelské roviny (UPF). Principy identifikace operátora a směrování APN-OI stále ovlivňují návrh výběru sítě a řezů (slice) v 5G.

## K čemu slouží

APN-OI byl vytvořen k řešení základního problému jednoznačné a nezaměnitelné identifikace síťové domény operátora v rámci globálního mobilního ekosystému za účelem směrování paketových dat. Před standardizovanými identifikátory, jako je APN-OI, bylo směrování dat ke správné síťové bráně, zejména v prostředí více operátorů a roamování, složité a náchylné k chybám. APN-OI poskytuje strukturovaný, globálně rozpoznatelný formát založený na již standardizovaných MCC a MNC, což umožňuje automatizovaný a spolehlivý výběr PGW.

Jeho zavedení bylo motivováno expanzí GPRS a později EPS, které vyžadovaly škálovatelné mechanismy pro podporu rostoucího počtu operátorů a stále složitějších roamingových dohod. Bez standardizovaného identifikátoru operátora v rámci APN by sítě musely spoléhat na proprietární nebo neškálovatelné metody pro určení cíle datové relace UE. To by bránilo globálnímu roamování, komplikovalo konfiguraci sítí a zvyšovalo riziko chybného směrování provozu. APN-OI elegantně využívá stávající systém identifikace PLMN (MCC/MNC) k vytvoření hierarchického jmenného prostoru v rámci DNS, což usnadňuje plynulá směrovací rozhodnutí.

APN-OI dále řeší potřebu vynucování politik a korelace účtování ve scénářích roamování. Jasnou identifikací domovského operátora může navštívená síť aplikovat správné politiky (např. účtování, QoS) na základě roamingové dohody. Umožňuje rozlišit mezi provozem směrovaným přes domovskou síť (kde je PGW v domovské síti) a místním průnikem (kde je PGW v navštívené síti), což jsou dvě základní roamingové architektury definované 3GPP. APN-OI tedy není pouze technickým identifikátorem, ale je základním kamenem pro komerční a provozní aspekty datových služeb mezi operátory.

## Klíčové vlastnosti

- Globálně jedinečná identifikace operátora založená na MCC a MNC
- Umožňuje deterministický výběr PGW během navazování spojení k PDN
- Základní prvek pro podporu architektur roamování s provozem přes domovskou síť i místním průnikem
- Přenášen v rámci standardizovaných protokolů 3GPP, jako je GTP a NAS
- Integruje se s DNS pro překlad síťových uzlů (např. konstrukce FQDN pro PGW)
- Poskytuje základ pro vynucování politik a účtování v scénářích mezi operátory

## Související pojmy

- [APN – Access Point Name](/mobilnisite/slovnik/apn/)
- [MCC – Mobile Country Code](/mobilnisite/slovnik/mcc/)
- [MNC – Mobile Network Code](/mobilnisite/slovnik/mnc/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)
- [DNN – Data Network Name](/mobilnisite/slovnik/dnn/)

## Definující specifikace

- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [APN-OI na 3GPP Explorer](https://3gpp-explorer.com/glossary/apn-oi/)
