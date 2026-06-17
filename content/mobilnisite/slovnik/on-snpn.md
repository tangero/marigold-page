---
slug: "on-snpn"
url: "/mobilnisite/slovnik/on-snpn/"
type: "slovnik"
title: "ON-SNPN – Onboarding Standalone Non-Public Network"
date: 2026-01-01
abbr: "ON-SNPN"
fullName: "Onboarding Standalone Non-Public Network"
category: "IoT"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/on-snpn/"
summary: "ON-SNPN je mechanismus 3GPP, který umožňuje zařízením IoT bezpečně objevit, ověřit a připojit se k samostatné neveřejné síti (SNPN) bez předchozích předplatitelských dat. Je klíčový pro nasazení masiv"
---

ON-SNPN je mechanismus 3GPP, který umožňuje zařízením IoT bezpečně objevit, ověřit a připojit se k samostatné neveřejné síti (Standalone Non-Public Network) bez předchozích předplatitelských dat.

## Popis

ON-SNPN je standardizovaný postup definovaný 3GPP pro zprovoznění (onboarding) zařízení v samostatné neveřejné síti (SNPN). SNPN je 5G síť provozovaná soukromým subjektem, která se neopírá o veřejnou pozemní mobilní síť (PLMN) pro funkce jádra sítě. Hlavní problém, který ON-SNPN řeší, je počáteční zajištění zařízení, která nemají platné předplatné nebo přihlašovací údaje pro cílovou SNPN. Architektura zahrnuje několik klíčových funkčních entit: zařízení žádající o přístup (User Equipment – UE), funkci pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) a autentizační server ([AUSF](/mobilnisite/slovnik/ausf/)) SNPN a onboardingovou síť ([ONN](/mobilnisite/slovnik/onn/)). ONN je samostatná, důvěryhodná síť, která usnadňuje počáteční připojení a zajištění přihlašovacích údajů.

Procedura ON-SNPN typicky začíná, když se UE nakonfigurované pro onboarding pokusí připojit k síti. UE vysílá registrační požadavek označující jeho onboardingový záměr. SNPN, která tento požadavek rozpozná, může UE přesměrovat na určenou ONN. ONN poskytuje omezený, počáteční přístup, často za použití generických nebo prozatímních přihlašovacích údajů. Prostřednictvím tohoto zabezpečeného kanálu pak UE komunikuje s onboardingovým serverem, který je součástí ekosystému SNPN nebo je jím důvěřován. Tento server ověří identitu zařízení (např. pomocí továrně nainstalovaného certifikátu) a zajistí mu potřebné přihlašovací údaje (jako je trvalý identifikátor předplatitele – SUPI a přidružené klíče) specifické pro cílovou SNPN.

Jakmile zařízení obdrží své SNPN-specifické přihlašovací údaje, může se odpojit od ONN a provést standardní registrační proceduru přímo s cílovou SNPN za použití nově zajištěných předplatitelských dat. AUSF SNPN tyto přihlašovací údaje ověří, čímž se dokončí autentizace. Tento proces je silně zabezpečen, aby se zabránilo útokům typu man-in-the-middle a krádeži přihlašovacích údajů, a využívá mechanismy jako autentizace zařízení založená na certifikátech a zabezpečené tunelování během přenosu přihlašovacích údajů. ON-SNPN je základním kamenem pro zajišťování bez zásahu operátora (zero-touch provisioning) v Průmyslu 4.0, neboť umožňuje bezproblémovou integraci senzorů, aktuátorů a dalších zařízení IoT do privátních 5G sítí bez manuálního zásahu.

## K čemu slouží

ON-SNPN byl vytvořen, aby vyřešil logistické a bezpečnostní výzvy nasazení rozsáhlého množství zařízení IoT v privátních 5G sítích (SNPN). Před jeho standardizací bylo zajišťování přihlašovacích údajů pro tisíce průmyslových zařízení manuálním, chybám podléhajícím a nejistým procesem, který často vyžadoval fyzický přístup nebo předzásobení síťově specifických klíčů již ve výrobě, což omezovalo flexibilitu dodavatelského řetězce. Potřeba automatizovaného, bezpečného a škálovatelného zprovoznění se stala kritickou s nástupem Průmyslu 4.0 a masivních nasazení IoT ve výrobě, logistice a energetice.

Tato technologie řeší omezení tradičních modelů předplatného založených na PLMN, které se nehodí pro soukromě vlastněné a provozované sítě. Umožňuje výrobcům zařízení vyrábět univerzální zařízení, aniž by je museli vázat na konkrétní zákaznickou síť během produkce. Místo toho bezpečný onboardingový proces umožňuje koncovému uživateli (operátorovi SNPN) převzít vlastnictví a zajistit přihlašovací údaje až po nasazení. Toto oddělení zefektivňuje dodavatelský řetězec a poskytuje provozní flexibilitu. Dále ON-SNPN zvyšuje bezpečnost tím, že zajišťuje, aby i počáteční, omezený přístup pro onboarding probíhal přes řízený a ověřený kanál, čímž zabraňuje neoprávněným zařízením v přístupu k hlavním prostředkům SNPN během fáze zajišťování.

## Klíčové vlastnosti

- Umožňuje automatické objevení a připojení k onboardingové síti (ONN) pro počáteční přístup
- Podporuje bezpečnou autentizaci zařízení pomocí předinstalovaných přihlašovacích údajů (např. certifikátů zařízení)
- Usnadňuje bezdrátové zajištění SNPN-specifických předplatitelských přihlašovacích údajů (SUPI, klíče)
- Umožňuje přesměrování ze SNPN na vyhrazenou ONN pro onboardingovou proceduru
- Poskytuje standardizované rozhraní mezi zařízením, ONN a serverem přihlašovacích údajů SNPN
- Zajišťuje, že onboardingový proces je z bezpečnostních důvodů izolován od provozní SNPN

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks

---

📖 **Anglický originál a plná specifikace:** [ON-SNPN na 3GPP Explorer](https://3gpp-explorer.com/glossary/on-snpn/)
