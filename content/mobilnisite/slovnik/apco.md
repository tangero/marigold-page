---
slug: "apco"
url: "/mobilnisite/slovnik/apco/"
type: "slovnik"
title: "APCO – Additional Protocol Configuration Options"
date: 2025-01-01
abbr: "APCO"
fullName: "Additional Protocol Configuration Options"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/apco/"
summary: "APCO je mechanismus v normách 3GPP, který umožňuje operátorům sítí konfigurovat další protokolové parametry nad rámec základního PDP kontextu. Umožňuje flexibilní konfiguraci protokolového zásobníku p"
---

APCO je mechanismus 3GPP, který umožňuje operátorům sítí konfigurovat další protokolové parametry nad rámec základního PDP kontextu pro flexibilní podporu uživatelských relací a služeb.

## Popis

Additional Protocol Configuration Options (APCO, volitelné parametry konfigurace dalších protokolů) je rámec pro konfiguraci protokolů definovaný v normách 3GPP, který rozšiřuje základní procedury pro vytvoření Packet Data Protocol (PDP) kontextu. Když mobilní zařízení navazuje datovou relaci se sítí, vytvoří PDP kontext definující základní parametry, jako je IP adresa, profil QoS a přístupový bod. APCO poskytuje standardizovaný způsob, jak do tohoto procesu aktivace nebo modifikace PDP kontextu zahrnout další parametry konfigurace specifické pro konkrétní protokol.

Mechanismus APCO funguje prostřednictvím zařazení specifických informačních elementů do protokolových zpráv mezi uživatelským zařízením (UE) a síťovými elementy, primárně mezi UE a Packet Data Network Gateway (PDN-GW) přes Serving Gateway (S-GW) a Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)). Tyto APCO parametry jsou transportovány transparentně přes páteřní síť a jsou interpretovány koncovými body za účelem vhodné konfigurace protokolových zásobníků. Rámec podporuje různé typy protokolů včetně IP, PPP a dalších sad protokolů, které mohou vyžadovat specifickou konfiguraci nad rámec základních parametrů konektivity.

Klíčové součásti APCO zahrnují strukturu informačního elementu APCO, která obsahuje identifikátory protokolů, délky konfiguračních dat a specifické hodnoty parametrů. Systém umožňuje podporu jak standardizovaných protokolů definovaných 3GPP, tak i vendor-specific nebo proprietárních protokolů pomocí příslušných rozsahů identifikátorů. Operátoři sítí mohou pomocí APCO implementovat funkce jako specifické parametry komprese hlaviček, podrobnosti konfigurace tunelů, volby metod autentizace nebo nastavení QoS specifická pro protokol, která nejsou pokryta základními parametry PDP kontextu.

Role APCO v síti je především role nosiče konfigurace pro rozšířené služby. Umožňuje síti podporovat rozmanité aplikace vyžadující specifické chování protokolů bez nutnosti samostatných signalizačních procedur. Například podnikové VPN služby mohou používat APCO ke konfiguraci specifických parametrů tunelování, zatímco IoT aplikace jej mohou využívat pro nastavení optimalizovaných schémat komprese hlaviček. Mechanismus zachovává zpětnou kompatibilitu tím, že je volitelný – relace bez požadavků na APCO používají standardní procedury PDP kontextu, zatímco relace potřebující dodatečnou konfiguraci transparentně zahrnují APCO parametry.

## K čemu slouží

APCO bylo vytvořeno, aby řešilo omezení základních parametrů PDP kontextu v podpoře stále složitějších síťových služeb a aplikací. Původní rámec PDP kontextu v normách 3GPP poskytoval pouze základní parametry konektivity, jako je přiřazení IP adresy a základní profily QoS. Jak se mobilní sítě vyvíjely, aby podporovaly podnikové služby, specializované aplikace a integraci zastaralých systémů, objevila se potřeba detailnějších možností konfigurace protokolů bez nutnosti přepracovat celou architekturu navazování relace.

Tato technologie řeší problém flexibility protokolového zásobníku v rámci standardizovaných mobilních sítí. Před zavedením APCO museli operátoři buď omezit služby na ty podporované základními PDP parametry, nebo implementovat proprietární rozšíření, která ohrožovala interoperabilitu. APCO poskytuje standardizovaný mechanismus, který umožňuje jak standardizované, tak proprietární konfigurace protokolů při zachování interoperability mezi zařízeními různých výrobců. To operátorům umožňuje nasazovat pokročilé služby, jako je optimalizované VPN připojení, specializované IoT protokoly nebo vylepšené konfigurace pro multimediální streamování, a zároveň zajišťuje, že zařízení UE a síťové vybavení od různých výrobců mohou správně spolupracovat.

Historicky byla motivací pro APCO rostoucí divergence mezi standardizovanými mobilními síťovými protokoly a různorodými požadavky reálných aplikací. Podnikoví zákazníci požadovali specifické parametry tunelování pro zabezpečenou konektivitu, zatímco nově vznikající IoT aplikace potřebovaly konfigurace odlehčených protokolů. APCO vytvořilo most mezi standardizovaným rámcem pro správu relací 3GPP a praktickými požadavky nasazených služeb, což umožňuje inovace v nabídce služeb bez narušení základní síťové architektury.

## Klíčové vlastnosti

- Rozšiřuje základní PDP kontext o další protokolové parametry
- Podporuje jak standardizované protokoly 3GPP, tak vendor-specific (výrobci specifické) protokoly
- Transparentní transport přes elementy páteřní sítě
- Volitelný mechanismus zachovávající zpětnou kompatibilitu
- Umožňuje pokročilou konfiguraci služeb bez samostatné signalizace
- Standardizovaná struktura informačního elementu pro interoperabilitu

## Definující specifikace

- **TS 23.380** (Rel-19) — IMS Restoration Procedures
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.826** (Rel-13) — P-CSCF Restoration Enhancements for WLAN

---

📖 **Anglický originál a plná specifikace:** [APCO na 3GPP Explorer](https://3gpp-explorer.com/glossary/apco/)
