---
slug: "lecp"
url: "/mobilnisite/slovnik/lecp/"
type: "slovnik"
title: "LECP – Liberty-Enabled Client or Proxy"
date: 2025-01-01
abbr: "LECP"
fullName: "Liberty-Enabled Client or Proxy"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/lecp/"
summary: "LECP je funkční entita definovaná v rámci projektu Liberty Alliance (LAP) pro správu federované identity. V kontextu 3GPP je zmiňována v souvislosti s vzájemným propojením sítí 3GPP a externích IP slu"
---

LECP je funkční entita z rámce Liberty Alliance, která umožňuje vzájemné propojení sítí 3GPP a externích IP služebních sítí s využitím protokolů Liberty pro federovanou autentizaci a jednotné přihlašování.

## Popis

Liberty-Enabled Client or Proxy (LECP) je koncept převzatý ze specifikací projektu Liberty Alliance ([LAP](/mobilnisite/slovnik/lap/)) do některých standardů 3GPP, především těch, které se zabývají vzájemným propojením sítí a přístupem k IP službám (např. propojení s [WLAN](/mobilnisite/slovnik/wlan/)). LECP není nativní síťová funkce 3GPP, ale role, kterou může uživatelské zařízení (UE) nebo mezilehlý síťový uzel zastávat při interakci s poskytovatelem služeb využívajícím protokoly Liberty Alliance. Jejím hlavním účelem je účastnit se transakcí federované identity, což umožňuje jednotné přihlašování ([SSO](/mobilnisite/slovnik/sso/)) a federaci identity napříč různými administrativními doménami.

Z architektonického hlediska LECP funguje jako zástupce koncového uživatele. Může jít o softwarovou komponentu na UE („klient“) nebo o síťovou entitu („proxy“), která protokoly Liberty zpracovává jménem jednoduššího klienta. V typické transakci Liberty LECP komunikuje s poskytovatelem identity (IdP) a poskytovatelem služeb ([SP](/mobilnisite/slovnik/sp/)). Usnadňuje výměnu autentizačních tvrzení (pomocí Security Assertion Markup Language – [SAML](/mobilnisite/slovnik/saml/)) a spravuje artefakty a cookies potřebné pro relaci SSO. Například ve scénáři propojení 3GPP-WLAN definovaném v TS 33.980 může UE (vystupující jako LECP) použít protokoly Liberty pro přístup k podnikové IP síti poté, co bylo autentizováno sítí 3GPP, která zde vystupuje jako IdP.

Jak to funguje, zahrnuje vícekrokový proces. Nejprve se uživatel autentizuje ve své domovské síti 3GPP. Při pokusu o přístup ke službě podporující Liberty přesměruje LECP na UE uživatelského agenta na Liberty IdP (kterým může být síť 3GPP). Po opětovné autentizaci (často transparentní díky SSO) IdP vydá SAML tvrzení. LECP toto tvrzení následně předloží cílovému poskytovateli služeb, aby získal přístup. Klíčovými zapojenými komponentami jsou samotný LECP, Liberty IdP, Liberty SP a podkladové protokoly jako Liberty [ID-FF](/mobilnisite/slovnik/id-ff/) (Identity Federation Framework) a SAML. V kontextu 3GPP je jeho role poskytnout standardizovanou metodu pro integraci přihlašovacích údajů 3GPP (jako je autentizace založená na [SIM](/mobilnisite/slovnik/sim/)) do širšího ekosystému webových a IP služeb využívajících standardy federované identity, čímž rozšiřuje dosah a pohodlí autentizace 3GPP.

## K čemu slouží

Účelem odkazování na LECP ve specifikacích 3GPP bylo umožnit bezproblémový a bezpečný přístup účastníků 3GPP ke službám třetích stran založeným na IP a k podnikovým sítím, zejména v období propojování s [WLAN](/mobilnisite/slovnik/wlan/) a rané konvergence mezi mobilními a internetovými službami. Před touto standardizací přístup k webové službě často vyžadoval samostatné uživatelské jméno a heslo, nesouvisející s mobilní identitou uživatele. Koncept LECP prostřednictvím rámce Liberty Alliance měl tento problém řešit tím, že umožňoval síti 3GPP vystupovat jako důvěryhodný poskytovatel identity, využívat svůj robustní autentizační mechanismus (např. pomocí SIM karty) k tomu, aby za uživatele ručila externím poskytovatelům služeb.

Tím se řešila významná omezení: zlepšil se uživatelský zážitek díky jednotnému přihlašování, snížila se únava z hesel a zvýšila se bezpečnost využitím silné síťové autentizace. Pro síťové operátory to představovalo přidanou hodnotu služby, která jim umožňovala zprostředkovávat vztahy důvěry s poskytovateli obsahu a podnikovými službami. Motivace pro jeho zařazení do 3GPP (kolem Rel-8) se časově shodovala s úsilím učinit systémy 3GPP otevřenějšími a interoperabilnějšími se širším ekosystémem internetové identity, který v té době zkoumal standardy federace, jako byly ty od Liberty Alliance a později OASIS SAML.

Definování role LECP dále poskytlo jasný architektonický zástupný symbol a soubor postupů pro to, jak se má UE nebo síťová proxy chovat v transakci Liberty. Tím byla zajištěna interoperabilita mezi zařízeními s podporou 3GPP a služebními sítěmi s podporou Liberty. I když konkrétní protokoly Liberty Alliance byly do značné míry nahrazeny pozdějšími standardy, jako je OpenID Connect, LECP představuje důležitý historický krok na cestě 3GPP k federované identitě a správě přístupu pro nepřístup 3GPP.

## Klíčové vlastnosti

- Funkční role definovaná projektem Liberty Alliance (LAP) pro federovanou identitu
- Může být implementována jako klient na uživatelském zařízení (UE) nebo jako síťová proxy
- Usnadňuje jednotné přihlašování (SSO) pomocí protokolů Liberty ID-FF a SAML
- Komunikuje s poskytovatelem identity Liberty (IdP) a poskytovatelem služeb (SP)
- Umožňuje využití přihlašovacích údajů 3GPP pro přístup k externím IP službám
- Zmiňována v 3GPP v souvislosti s propojováním s WLAN a přístupem k IP služebním sítím

## Související pojmy

- [SAML – Security Assertion Markup Language](/mobilnisite/slovnik/saml/)

## Definující specifikace

- **TR 33.980** (Rel-19) — GAA & Liberty Alliance Interworking Guidelines

---

📖 **Anglický originál a plná specifikace:** [LECP na 3GPP Explorer](https://3gpp-explorer.com/glossary/lecp/)
