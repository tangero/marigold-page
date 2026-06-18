---
slug: "rid"
url: "/mobilnisite/slovnik/rid/"
type: "slovnik"
title: "RID – Remote Identification"
date: 2026-01-01
abbr: "RID"
fullName: "Remote Identification"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rid/"
summary: "Vzdálená identifikace (Remote Identification) je služba, která umožňuje síti vzdáleně identifikovat a autentizovat uživatele nebo zařízení, často používaná pro zabezpečený přístup ke službám bez fyzic"
---

RID je služba 3GPP, která umožňuje síti vzdáleně identifikovat a autentizovat uživatele nebo zařízení, podporuje zabezpečený přístup, ochranu soukromí a poskytování služeb pro IoT a veřejnou bezpečnost v 5G.

## Popis

Vzdálená identifikace (RID) je servisní schopnost definovaná v 3GPP, která umožňuje síťové entitě, jako je aplikační server nebo poskytovatel služeb, vzdáleně identifikovat a autentizovat uživatelské zařízení (UE) nebo uživatele bez nutnosti přímého fyzického přístupu nebo zásahu uživatele. Toho je dosaženo pomocí kryptografických protokolů a síťově asistovaných procedur, které využívají přihlašovací údaje předplatného UE nebo dočasné identifikátory. RID funguje v rámci servisně orientované architektury 5G a zapojuje funkce jádra sítě, jako je Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)), Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) a Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)). Služba umožňuje zabezpečenou identifikaci s ochranou soukromí pro různé případy užití, jako je přístup ke službám založeným na poloze, ověření integrity zařízení pro nasazení IoT nebo umožnění anonymní autentizace pro komunikaci veřejné bezpečnosti.

Z architektonického hlediska je RID specifikována v dokumentu 3GPP TS 23.256 a souvisejících dokumentech, které popisují, jak mohou externí aplikace požadovat identifikaci prostřednictvím NEF, který slouží jako zprostředkovatel pro ochranu vnitřních částí sítě. Proces typicky zahrnuje odeslání žádosti od aplikace s parametry, jako je dočasný identifikátor nebo přihlašovací údaje specifické pro službu, které síť po řádné autorizaci a kontrolách ochrany soukromí namapuje na trvalý identifikátor předplatného (např. [SUPI](/mobilnisite/slovnik/supi/)). Mezi klíčové komponenty patří poskytovatel služby RID, který žádost iniciuje, a jádrová síť 5G, která identifikaci provádí pomocí procedur autentizace a dohody klíčů ([AKA](/mobilnisite/slovnik/aka/)) nebo podobných mechanismů. RID může spolupracovat s technologiemi zvyšujícími soukromí, jako jsou subscription concealed identifiers ([SUCI](/mobilnisite/slovnik/suci/)), aby zabránila sledování, a zajišťuje, že identifikace je provedena pouze při autorizaci a v případě potřeby.

Jak RID funguje, zahrnuje několik kroků: nejprve externí aplikace (např. služba chytrého města) požádá prostřednictvím NEF o identifikaci UE a poskytne token nebo identifikátor, který si UE předtím vyměnila během registrace služby. NEF ověří přihlašovací údaje aplikace a předá žádost příslušným funkcím jádra, jako je UDM nebo AUSF, které načtou profil UE a v případě potřeby provedou autentizaci. Síť poté vrátí aplikaci ověřenou identitu nebo atributy (např. potvrzený věk nebo typ zařízení) bez vystavení citlivých dat účastníka. Tento proces podporuje jak online, tak offline režimy s volitelnými mechanismy souhlasu uživatele pro soulad s předpisy, jako je GDPR. RID je zvláště cenná ve scénářích IoT, kde je třeba identifikovat zařízení pro přístup ke službám bez lidské interakce, a v nouzových situacích, kdy musí záchranáři rychle autentizovat zařízení v oblasti katastrofy.

## K čemu slouží

RID byla zavedena, aby řešila rostoucí potřebu zabezpečené vzdálené autentizace v ekosystémech 5G, zejména s rozšířením zařízení a služeb IoT, které vyžadují automatizovanou identifikaci bez fyzické přítomnosti. Předchozí přístupy se často spoléhaly na manuální procesy nebo méně zabezpečené metody, jako je identifikace založená na IP, které byly nedostatečné pro škálovatelné aplikace citlivé na soukromí. RID poskytuje standardizovaný způsob, jak mohou poskytovatelé služeb ověřovat identity prostřednictvím mobilní sítě, a využívá robustní bezpečnostní infrastrukturu systémů 3GPP, což řeší problémy jako falšování identity, neoprávněný přístup a porušování soukromí.

Historicky motivace pro RID vzešla z případů užití ve verzi 17, jako je identifikace [UAV](/mobilnisite/slovnik/uav/) (dronů) pro regulatorní soulad, kde letecké úřady vyžadují vzdálené ověření létajících zařízení. Podporuje také aplikace veřejné bezpečnosti, kde záchranné služby potřebují identifikovat zařízení v krizi bez narušení soukromí uživatelů. Vytvořením síťové identifikační služby umožňuje 3GPP nové obchodní modely, jako je ověření věku pro digitální služby nebo atestace zařízení pro průmyslové IoT, při zachování vysokých standardů zabezpečení a ochrany soukromí očekávaných v mobilních sítích. Tím se řeší omezení předchozích ad-hoc řešení integrací identifikace přímo do jádra 5G, což zajišťuje interoperabilitu a důvěru napříč různými operátory a poskytovateli služeb.

## Klíčové vlastnosti

- Umožňuje vzdálenou identifikaci UE nebo uživatelů prostřednictvím síťově asistovaných procedur
- Podporuje ochranu soukromí pomocí mechanismů jako SUCI a souhlas uživatele
- Integruje se s servisně orientovanou architekturou 5G prostřednictvím Network Exposure Function (NEF)
- Usnadňuje zabezpečenou autentizaci pro případy užití IoT, veřejné bezpečnosti a regulatorního souladu
- Umožňuje externím aplikacím požadovat identifikaci bez přístupu k vnitřním částem jádra sítě
- Podporuje jak online režim identifikace v reálném čase, tak offline režimy

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [SUCI – Subscription Concealed Identifier](/mobilnisite/slovnik/suci/)
- [UAV – Uncrewed Aerial Vehicle](/mobilnisite/slovnik/uav/)

## Definující specifikace

- **TS 23.256** (Rel-19) — UAS Support Architecture Enhancements
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.754** (Rel-17) — Study on UAS Connectivity, ID & Tracking
- **TS 29.256** (Rel-19) — UAS-NF Stage 3 Protocol Specification
- **TS 33.535** (Rel-19) — 5G AKMA: Authentication and Key Management for Apps

---

📖 **Anglický originál a plná specifikace:** [RID na 3GPP Explorer](https://3gpp-explorer.com/glossary/rid/)
