---
slug: "ssos"
url: "/mobilnisite/slovnik/ssos/"
type: "slovnik"
title: "SSOS – SSO Service"
date: 2025-01-01
abbr: "SSOS"
fullName: "SSO Service"
category: "Services"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/ssos/"
summary: "Služba SSO (SSOS) označuje konkrétní nabídku služby nebo schopnost, která implementuje funkci jednotného přihlašování v rámci sítě 3GPP. Představuje konkrétní realizaci rámce SSO a poskytuje infrastru"
---

SSOS je konkrétní nabídkou služby, která implementuje funkci jednotného přihlašování (Single Sign-On) v rámci sítě 3GPP a poskytuje infrastrukturu a rozhraní pro autentizaci a autorizaci.

## Popis

Služba [SSO](/mobilnisite/slovnik/sso/) (SSOS) je operační instancí konceptu jednotného přihlašování (SSO) v systému 3GPP. Zahrnuje kompletní sadu síťových funkcí, protokolů a rozhraní potřebných k poskytnutí SSO jako použitelné služby účastníkům a poskytovatelům služeb třetích stran. Zatímco SSO definuje architektonické principy, SSOS odkazuje na nasaditelnou službu, která tyto principy provádí. Slouží jako zprostředkovatel, který zprostředkovává důvěru mezi poskytovatelem identity uživatele (typicky domácí sítí) a různými poskytovateli služeb ([SP](/mobilnisite/slovnik/sp/)), ke kterým se uživatel chce přihlásit.

Technicky je SSOS implementována prostřednictvím vyhrazených funkčních prvků, často spolulokalizovaných nebo integrovaných do stávajících síťových uzlů. Základní součástí je funkce služby SSO, která zahrnuje logiku pro správu relací, generování tokenů (pomocí standardů jako [SAML](/mobilnisite/slovnik/saml/) nebo OpenID Connect) a vynucování politik. Spolupracuje s autentizační infrastrukturou, jako je Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)), pro ověření přihlašovacích údajů uživatele. Také zpřístupňuje standardizovaná rozhraní (např. založená na Diameter nebo [HTTP](/mobilnisite/slovnik/http/)/2) pro poskytovatele služeb, aby mohli požadovat autentizaci a ověřovat tokeny.

Služba funguje tak, že zachycuje přístupové požadavky na chráněné služby. Když dorazí neautentizovaný požadavek, SSOS přesměruje uživatelský agent na autentizační portál. Po úspěšné autentizaci (např. pomocí [SIM](/mobilnisite/slovnik/sim/), hesla nebo biometrie) SSOS vytvoří zabezpečenou relaci a vydá kryptografický token. Tento token je pak použit k bezproblémovému přístupu k dalším službám bez opětovného přihlášení, protože SSOS ověřuje token pro každý následující požadavek. Služba spravuje celý životní cyklus, včetně expirace, obnovení a odvolání tokenů.

Klíčovou rolí SSOS je její funkce ve federaci služeb. Udržuje vztah důvěry s externími SP, často navázaný prostřednictvím předem sdílených certifikátů nebo dynamických protokolů pro zjišťování. SSOS také zpracovává souhlas uživatele, protokolování a auditování, aby splnila regulatorní požadavky. V kontextu 5G může být SSOS implementována jako síťová funkce v rámci architektury založené na službách ([SBA](/mobilnisite/slovnik/sba/)), která komunikuje s funkcí Network Repository Function (NRF) pro zjišťování a s Security Edge Protection Proxy (SEPP) pro zabezpečení mezi sítěmi.

## K čemu slouží

Služba SSO byla vytvořena, aby poskytla standardizovanou, provozovatelnou vrstvu služeb pro jednotné přihlašování, což znamená posun od teoretických rámců k praktickému nasazení. Zatímco specifikace SSO definovaly 'co', SSOS řeší 'jak' tím, že podrobně popisuje charakteristiky služby, provozní postupy a aspekty správy. Řeší problém nekonzistentních a proprietárních implementací SSO, které bránily interoperabilitě mezi různými síťovými operátory a poskytovateli služeb.

Před její specifikací čelili operátoři vyvíjející schopnosti SSO nejednoznačnosti v implementačních detailech, což vedlo k fragmentovaným uživatelským zkušenostem a zvýšeným integračním nákladům pro vývojáře aplikací. SSOS poskytuje jasný plán pro vybudování kompatibilní služby SSO, který zajišťuje konzistentní implementaci všech nezbytných komponent – jako jsou formáty tokenů, zpracování chyb a rozhraní pro účtování. To umožňuje vznik trhu interoperabilních služeb, kde mohou uživatelé využívat svou mobilní identitu v širokém ekosystému.

Motivovaná komerční potřebou zpeněžit autentizační aktiva sítě umožňuje SSOS operátorům nabízet SSO jako přidanou službu podnikům a poskytovatelům obsahu. Usnadňuje nové obchodní modely, jako je identita jako služba. Standardizací služby zajistila 3GPP jednotné uplatňování bezpečnostních a ochranných kontrol, které chrání uživatelská data ve federovaných prostředích. V podstatě přeměňuje bezpečnostní rámec SSO na fakturovatelnou, spravovatelnou síťovou službu.

## Klíčové vlastnosti

- Provozní implementace služby rámce SSO
- Standardizovaná rozhraní pro integraci poskytovatelů služeb a ověření tokenů
- Komplexní správa životního cyklu relací a tokenů (vydání, obnovení, odvolání)
- Integrace se síťovými autentizačními systémy (HSS/UDM, AUSF)
- Podpora federované identity a správy důvěry s externími doménami
- Schopnosti účtování a vynucování politik pro komerční nabídky služeb

## Definující specifikace

- **TR 33.980** (Rel-19) — GAA & Liberty Alliance Interworking Guidelines

---

📖 **Anglický originál a plná specifikace:** [SSOS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ssos/)
