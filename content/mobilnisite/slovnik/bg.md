---
slug: "bg"
url: "/mobilnisite/slovnik/bg/"
type: "slovnik"
title: "BG – Border Gateway"
date: 2025-01-01
abbr: "BG"
fullName: "Border Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bg/"
summary: "Border Gateway (BG) je funkční entita v sítích GPRS/UMTS, která zajišťuje propojení a zabezpečení mezi páteřní sítí GPRS a externími paketovými datovými sítěmi (PDN). Funguje jako brána, která obstará"
---

BG je funkční entita v sítích GPRS/UMTS, která slouží jako zabezpečená brána mezi páteřní sítí GPRS a externími paketovými datovými sítěmi a zajišťuje IP směrování, překlad adres a funkce firewallu.

## Popis

Border Gateway (BG) je klíčová architektonická komponenta v jádru sítě [GPRS](/mobilnisite/slovnik/gprs/), konkrétně součást funkce Gateway GPRS Support Node (GGSN) nebo implementovaná jako samostatný uzel. Jejím hlavním úkolem je sloužit jako demarkační bod mezi zabezpečenou, operátorem řízenou páteřní sítí GPRS (doménou založenou na GPRS Tunneling Protocolu neboli [GTP](/mobilnisite/slovnik/gtp/)) a externími, nedůvěryhodnými paketovými datovými sítěmi, jako je veřejný internet nebo firemní intranety. BG vynucuje bezpečnostní politiky, provádí překlad síťových adres ([NAT](/mobilnisite/slovnik/nat/)) a spravuje IP směrování, aby zajistil správné přeposílání datových paketů mezi mobilním zařízením uživatele ([MS](/mobilnisite/slovnik/ms/)) a cílovou [PDN](/mobilnisite/slovnik/pdn/).

Z architektonického hlediska je BG interně propojen s dalšími uzly sítě GPRS, především s GGSN, přes referenční bod Gi. Externě se připojuje k PDN. Funguje na IP vrstvě, kde kontroluje a zpracovává IP pakety. Mezi klíčové funkční komponenty patří firewall pro filtrování paketů a řízení přístupu, modul NAT pro překlad mezi privátními IP adresami páteřní sítě GPRS a veřejnými IP adresami používanými na externích sítích a směrovací funkce pro určení optimální cesty pro datový provoz. Může také zahrnovat funkce účtovací brány pro sběr záznamů o využití dat pro účely fakturace.

Během provozu, když mobilní zařízení aktivuje kontext Packet Data Protocol ([PDP](/mobilnisite/slovnik/pdp/)), GGSN mu přidělí IP adresu z adresního prostoru sítě GPRS. Odchozí provoz ze stanice je tunelován přes GTP k GGSN, který pak předá IP pakety BG. BG provede potřebný NAT, nahradí privátní zdrojovou IP adresu veřejnou, uplatní pravidla firewallu a směruje paket do externí PDN. Pro příchozí provoz určený pro mobilní zařízení probíhá opačný proces: BG přijímá pakety, přeloží veřejnou cílovou IP adresu na odpovídající privátní IP adresu a přepošle je GGSN pro GTP tunelování k Serving GPRS Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) a nakonec do rádiové přístupové sítě. Tato architektura izoluje jádro GPRS od externích hrozeb a řeší nedostatek IP adres.

## K čemu slouží

Border Gateway byl zaveden ve 3GPP Release 99, aby řešil základní výzvy v zabezpečeném a efektivním propojení mobilních sítí s externími IP sítěmi, protože [GPRS](/mobilnisite/slovnik/gprs/) umožnilo paketově přepínané datové služby. Před GPRS byly mobilní sítě primárně okruhově přepínané pro hlas, s omezenými datovými schopnostmi. Přechod na paketová data vyžadoval zabezpečenou bránu, která by propojila soukromou síťovou doménu operátora s veřejnými datovými sítěmi a chránila síťovou infrastrukturu a data účastníků před externími útoky.

Řešil několik klíčových problémů: Za prvé poskytoval základní zabezpečení prostřednictvím funkce firewallu, které bránilo neautorizovanému přístupu z internetu do jádra GPRS. Za druhé umožnil efektivní využití omezeného množství veřejných IPv4 adres pomocí překladu síťových adres (NAT), což umožnilo mnoha mobilním zařízením sdílet společný fond veřejných IP adres. Za třetí spravoval směrování mezi různými administrativními doménami, aby zajistil správný průchod paketů z mobilní sítě do různých externích PDN (např. internet, IMS, firemní sítě). Vytvoření BG bylo motivováno potřebou standardizovaného, řízeného rozhraní (referenční bod Gi), které by mohlo podporovat různé služby, jako je WAP prohlížení, e-mail a později IMS multimédia, při zachování kontroly operátora nad zabezpečením, účtováním a vynucováním politik.

## Klíčové vlastnosti

- Firewall a filtrování paketů pro zabezpečení mezi páteřní sítí GPRS a externími PDN
- Překlad síťových adres (NAT) pro šetření veřejnými IPv4 adresami
- IP směrování a správa propojení pro externí paketové datové sítě
- Podpora specifikace rozhraní referenčního bodu Gi
- Integrace s účtovacími systémy pro evidenci využití dat
- Řízení provozu a potenciální označování QoS na hranici sítě

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [NAT – Network Address Translation](/mobilnisite/slovnik/nat/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.622** (Rel-11) — Generic Network Resources IRP NRM
- **TS 32.632** (Rel-11) — Core Network Resources IRP: Network Resource Model
- **TS 32.732** (Rel-11) — IMS Network Resource Model IRP: Information Service
- **TS 33.210** (Rel-19) — UMTS Security for IP Networks

---

📖 **Anglický originál a plná specifikace:** [BG na 3GPP Explorer](https://3gpp-explorer.com/glossary/bg/)
