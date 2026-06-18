---
slug: "wpki"
url: "/mobilnisite/slovnik/wpki/"
type: "slovnik"
title: "WPKI – Wireless Public Key Infrastructure"
date: 2025-01-01
abbr: "WPKI"
fullName: "Wireless Public Key Infrastructure"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/wpki/"
summary: "Infrastruktura veřejného klíče (PKI) přizpůsobená omezením bezdrátových sítí a mobilních zařízení. Umožňuje bezpečnou správu digitálních certifikátů, klíčů a vztahů důvěry pro aplikace jako mobilní ob"
---

WPKI je infrastruktura veřejného klíče přizpůsobená pro bezdrátové sítě a mobilní zařízení, která umožňuje bezpečnou správu digitálních certifikátů a klíčů pro aplikace jako mobilní obchodování a autentizaci v systémech 3GPP.

## Popis

Wireless Public Key Infrastructure (WPKI) je soubor standardů a protokolů, které rozšiřují tradiční koncepty [PKI](/mobilnisite/slovnik/pki/) do mobilního prostředí a řeší jeho omezení, jako je výpočetní výkon zařízení, paměť, šířka pásma a přerušované spojení. Poskytuje základ pro vydávání, správu, distribuci, používání, ukládání a odvolávání digitálních certifikátů pro mobilní účastníky a síťové entity. Mezi základní komponenty patří certifikační autorita ([CA](/mobilnisite/slovnik/ca/)), která certifikáty vydává, registrační autorita ([RA](/mobilnisite/slovnik/ra/)), která ověřuje identitu účastníka, úložiště pro ukládání certifikátů a seznamů odvolaných certifikátů ([CRL](/mobilnisite/slovnik/crl/)) a koncové entity vybavené bezdrátovými identifikačními moduly (jako [USIM](/mobilnisite/slovnik/usim/)) nebo softwarovými certifikáty.

Jak to funguje: Zahrnuje optimalizované protokoly pro registraci a správu certifikátů. Mobilní zařízení prostřednictvím své uživatelské stanice (UE) typicky iniciuje žádost o certifikát přes zabezpečený kanál k WPKI portálu nebo RA. Žádost může být vygenerována pomocí páru klíčů vytvořeného na zařízení nebo, pro vyšší zabezpečení, uvnitř odolného modulu UICC. RA ověří identitu účastníka, často s využitím stávající autentizace mobilní sítě (např. pomocí [IMSI](/mobilnisite/slovnik/imsi/)). Po schválení CA certifikát vydá, ten je pak doručen do zařízení a uložen. Pro ověřování platnosti certifikátů WPKI často používá komprimované formáty certifikátů (jako certifikáty [WTLS](/mobilnisite/slovnik/wtls/)) a účinné mechanismy kontroly stavu, jako jsou respondéry Online Certificate Status Protocol ([OCSP](/mobilnisite/slovnik/ocsp/)), aby se zabránilo stahování rozsáhlých CRL přes rozhraní.

Její role v síti je umožnit důvěryhodné služby vyžadující nepopiratelnost, integritu a důvěrnost. WPKI usnadňuje zabezpečené mobilní bankovnictví, úřední elektronické podpisy, přístup k podnikovým VPN a autentizaci zařízení vůči síti nad rámec nativní 3GPP AKA. Integruje se s architekturou Generic Bootstrapping Architecture (GBA) pro využití sdíleného tajemství v UICC k zabezpečení počáteční fáze registrace PKI. Z architektonického hlediska často spolupracuje s domácím prostředím a síťovými aplikačními servery a poskytuje standardizovaný kořen důvěry, který poskytovatelům služeb umožňuje spolehlivě a právně závazně ověřit identitu mobilního uživatele, čímž překlenuje propast mezi telekomunikační autentizací a širšími internetovými bezpečnostními službami.

## K čemu slouží

WPKI byla vytvořena, aby umožnila pokročilé bezpečnostní služby v mobilních sítích, které vyžadují právní a technické záruky poskytované digitálními certifikáty, které samotná nativní SIM-based autentizace nepodporovala. Tradiční PKI byla navržena pro pevný internet s výkonnými PC a stabilním připojením, což ji činilo nevhodnou pro raná mobilní zařízení s omezenými možnostmi. Problém, který WPKI řeší, je, jak přinést silnou autentizaci, digitální podpisy a správu šifrovacích klíčů na masový mobilní trh.

Motivace vycházela z růstu mobilních datových služeb a vize mobilního elektronického obchodu, m-government a zabezpečeného podnikového přístupu. Operátoři a poskytovatelé služeb potřebovali způsob, jak uživatele pro transakce nad rámec síťového přístupu jedinečně a bezpečně identifikovat. Mezi omezení předchozích přístupů patřila vysoká režie certifikátů X.509 na pomalých bezdrátových spojích a absence standardizovaného způsobu správy životního cyklu certifikátů na omezených zařízeních. WPKI tyto procesy standardizovala a definovala optimalizované formáty certifikátů a odlehčené protokoly.

Historicky zavedená v 3GPP Release 6 reagovala WPKI na tržní poptávku po standardizovaných mobilních bezpečnostních rámcích. Vyřešila propast mezi uzavřenou, na operátora zaměřenou bezpečností SIM karty a otevřenou, certifikátovou bezpečností vyžadovanou pro internetové aplikace. Přizpůsobením PKI bezdrátovému světu umožnila mobilním sítím stát se důvěryhodnou platformou pro širokou škálu zabezpečených služeb, usnadnila nové obchodní modely a splnila regulační požadavky na elektronické podpisy v mnoha jurisdikcích.

## Klíčové vlastnosti

- Optimalizované formáty certifikátů (např. WTLS, kompaktní X.509) pro efektivitu šířky pásma
- Integrace s UICC/USIM pro bezpečné uložení a generování klíčů
- Definované postupy registrace a správy certifikátů pro mobilní zařízení
- Podpora Online Certificate Status Protocol (OCSP) pro účinnou kontrolu odvolání
- Soulad s 3GPP Generic Bootstrapping Architecture (GBA) pro zabezpečený bootstrap
- Umožňuje mobilní digitální podpisy a nepopiratelnost pro aplikace

## Související pojmy

- [PKI – Public Key Infrastructure](/mobilnisite/slovnik/pki/)
- [GBA – Generic Bootstrapping Architecture](/mobilnisite/slovnik/gba/)
- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)

## Definující specifikace

- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3

---

📖 **Anglický originál a plná specifikace:** [WPKI na 3GPP Explorer](https://3gpp-explorer.com/glossary/wpki/)
