---
slug: "ocsp"
url: "/mobilnisite/slovnik/ocsp/"
type: "slovnik"
title: "OCSP – Online Certificate Status Protocol"
date: 2025-01-01
abbr: "OCSP"
fullName: "Online Certificate Status Protocol"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/ocsp/"
summary: "Internetový protokol používaný pro získávání stavu odvolání certifikátů X.509 v reálném čase. V sítích 3GPP je přijat pro bezpečnou správu přihlašovacích údajů, což umožňuje síťovým funkcím a uživatel"
---

OCSP je internetový protokol používaný v sítích 3GPP pro ověřování stavu odvolání digitálních certifikátů X.509 v reálném čase za účelem zajištění bezpečné správy přihlašovacích údajů.

## Popis

Online Certificate Status Protocol (OCSP) je standard [IETF](/mobilnisite/slovnik/ietf/) (RFC 6960) přijatý ve specifikacích 3GPP, který poskytuje validaci stavu odvolání certifikátů veřejného klíče v reálném čase. V infrastruktuře veřejného klíče (PKI) mohou být certifikáty odvolány před datem své expirace z důvodu kompromitace privátního klíče nebo jiných problémů. OCSP poskytuje efektivnější a včasnější alternativu k tradičním seznamům odvolaných certifikátů ([CRL](/mobilnisite/slovnik/crl/)). Protokol funguje v modelu klient-server: klient OCSP (označovaný jako žadatel) odešle požadavek na stav konkrétního certifikátu k odpovídači OCSP (serveru). Odpovídač, který je typicky provozován certifikační autoritou ([CA](/mobilnisite/slovnik/ca/)) nebo delegovanou entitou, zkontroluje svou databázi odvolání a vrátí digitálně podepsanou odpověď udávající stav certifikátu: 'good' (platný), 'revoked' (odvolaný) nebo 'unknown' (neznámý).

V rámci architektur 3GPP je OCSP integrován do různých bezpečnostních rámců. Například v obecné bootstrapové architektuře ([GBA](/mobilnisite/slovnik/gba/)) může být OCSP používán síťovými aplikačními funkcemi ([NAF](/mobilnisite/slovnik/naf/)) nebo bootstrapovou serverovou funkcí ([BSF](/mobilnisite/slovnik/bsf/)) k validaci certifikátů předložených uživatelským zařízením (UE) nebo jinými síťovými prvky. Zprávy protokolu jsou typicky přenášeny přes [HTTP](/mobilnisite/slovnik/http/). Požadavek OCSP obsahuje identifikátor daného certifikátu (často hash jeho sériového čísla a jména vydavatele). Odpověď OCSP je podepsána klíčem odpovídače a klient musí tento podpis ověřit pomocí důvěryhodného certifikátu odpovídače. 3GPP profiluje použití OCSP, specifikuje povinná rozšíření certifikátů, přijatelné kryptografické algoritmy a požadavky na ukládání odpovědí do mezipaměti pro snížení zátěže odpovídače.

Jeho role je klíčová pro udržení řetězce důvěry v bezpečnostních systémech 3GPP, které spoléhají na PKI, jako je zabezpečení rozhraní v servisně orientované architektuře 5G (SBA), pro autentizaci v IoT scénářích používajících přihlašovací údaje jako SUCI/SUPI a pro validaci certifikátů v multimediálních subsystémech. Tím, že umožňuje okamžitou kontrolu odvolání, OCSP zmírňuje riziko spoléhání se na kompromitovaný certifikát, což je významná bezpečnostní hrozba. Je to základní komponenta pro dynamickou správu důvěry v moderních automatizovaných mobilních sítích.

## K čemu slouží

OCSP byl integrován do standardů 3GPP, aby řešil omezení seznamů odvolaných certifikátů ([CRL](/mobilnisite/slovnik/crl/)) v dynamických mobilních prostředích. CRL jsou periodicky publikované seznamy všech odvolaných certifikátů, které si klienti musí stáhnout a zpracovat. Tento model má významné nevýhody: zavádí latenci (protože klienti mohou používat zastaralé seznamy), spotřebovává šířku pásma (zejména u velkých seznamů) a dobře se neškáluje pro zařízení s omezenými zdroji. V rychlých mobilních sítích, kde zařízení roamují a služby jsou vytvářeny na vyžádání, je často nezbytná kontrola odvolání téměř v reálném čase.

Protokol řeší problém včasné a efektivní validace stavu certifikátu. Umožňuje síťové entitě dotázat se na stav jednotlivého certifikátu přesně v okamžiku, kdy je potřeba rozhodnutí o důvěře, a poskytuje tak mnohem čerstvější informace než CRL. To je zásadní pro bezpečnostně citlivé operace, jako je počáteční autentizace pro přístup k síti, navazování zabezpečených tunelů nebo validace softwarových aktualizací. Jeho přijetí v 3GPP bylo motivováno rostoucí závislostí na PKI pro autentizaci síťových funkcí ve všech-IP architekturách (jako IMS a 5G SBA) a pro zabezpečení přihlašovacích údajů IoT zařízení. OCSP poskytuje agilitu vyžadovanou pro automatizované, bezobslužné zřizování a provoz v těchto komplexních ekosystémech, kde se bezpečnostní stav může rychle měnit.

## Klíčové vlastnosti

- Dotazování na stav odvolání jednotlivých certifikátů v reálném čase.
- Vrací podepsané odpovědi: good (platný), revoked (odvolaný) nebo unknown (neznámý).
- Snižuje spotřebu šířky pásma a latenci ve srovnání se stahováním celých CRL.
- Podporuje ukládání odpovědí do mezipaměti s definovanou aktuálností (pole nextUpdate).
- Integrován do bezpečnostních architektur 3GPP, jako je GBA a SBA.
- Pro přenos zpráv protokolu používá HTTP/HTTPS.

## Definující specifikace

- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 33.310** (Rel-19) — 3GPP Authentication Framework for Network Nodes
- **TS 33.320** (Rel-19) — H(e)NB Subsystem Security Architecture
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.812** (Rel-9) — M2M Remote Subscription Management Security
- **TR 33.876** (Rel-18) — Technical Report on Certificate Management
- **TR 33.938** (Rel-19) — 3GPP Cryptographic Inventory for 5G

---

📖 **Anglický originál a plná specifikace:** [OCSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ocsp/)
