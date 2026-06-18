---
slug: "pca"
url: "/mobilnisite/slovnik/pca/"
type: "slovnik"
title: "PCA – Pseudonym Certificate Authority"
date: 2025-01-01
abbr: "PCA"
fullName: "Pseudonym Certificate Authority"
category: "Security"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pca/"
summary: "Důvěryhodná entita v bezpečnostní architektuře V2X (Vehicle-to-Everything) podle 3GPP, která vydává pseudonymní certifikáty vozidlům. Tyto certifikáty chrání identitu vozidla a soukromí polohy a zárov"
---

PCA je důvěryhodná entita v bezpečnostní architektuře V2X podle 3GPP, která vydává pseudonymní certifikáty vozidlům za účelem ochrany jejich identity a soukromí polohy, a zároveň umožňuje bezpečnou autentizaci.

## Popis

Autorita pro pseudonymní certifikáty (PCA) je klíčová bezpečnostní komponenta v rámci architektury 3GPP pro komunikaci Vehicle-to-Everything ([V2X](/mobilnisite/slovnik/v2x/)). Funguje jako specializovaná certifikační autorita ([CA](/mobilnisite/slovnik/ca/)), která vydává vozidlům (nebo uživatelským zařízením ve vozidlech) krátkodobé, často se měnící pseudonymní certifikáty. Tyto certifikáty umožňují vozidlu autentizovat své zprávy (např. [CAM](/mobilnisite/slovnik/cam/), [DENM](/mobilnisite/slovnik/denm/)) v sítích V2X bez odhalení své dlouhodobé identity, čímž chrání soukromí řidiče. PCA funguje v rámci infrastruktury veřejných klíčů ([PKI](/mobilnisite/slovnik/pki/)) přizpůsobené pro V2X, často definované ve standardech jako [ETSI](/mobilnisite/slovnik/etsi/) [ITS](/mobilnisite/slovnik/its/).

Architektonicky je PCA typicky součástí hierarchické PKI, která zahrnuje kořenovou CA a případně i mezilehlé CA. Palubní jednotka (OBU) vozidla žádá o dávky pseudonymních certifikátů od PCA prostřednictvím zabezpečených spojení (např. přes mobilní sítě). Každý certifikát obsahuje veřejný klíč a je platný po omezenou dobu (např. od minut po týdny). Odpovídající soukromé klíče jsou bezpečně uloženy v hardwarovém bezpečnostním modulu (HSM) vozidla. Samotná PCA musí být vysoce dostupná a zabezpečená, protože zpracovává citlivý klíčový materiál.

Jak to funguje: Vozidlo se nejprve zaregistruje u autority pro dlouhodobé certifikáty (LTCA), aby získalo registrační certifikát. Pomocí něj se autentizuje u PCA a žádá o sadu pseudonymních certifikátů. PCA žádost ověří, vygeneruje certifikáty a podepíše je svým soukromým klíčem. Vozidlo pak tyto certifikáty používá k podepisování zpráv V2X a pravidelně je obměňuje, aby se zabránilo sledování. Přijímající vozidla ověřují podpisy pomocí veřejného klíče PCA, který je distribuován prostřednictvím certifikátů od kořenové CA. Tento proces zajišťuje integritu a autenticitu zpráv při zachování anonymity.

Její role v síti 3GPP spočívá v umožnění bezpečných a na soukromí dbajících služeb V2X přes rozhraní mobilních sítí (např. PC5, Uu). PCA spolupracuje s dalšími síťovými funkcemi, jako je řídicí funkce V2X pro autorizaci. Je klíčovým prvkem pro zabezpečení V2X založené na 3GPP, který zajišťuje, že bezpečnostně kritické zprávy jsou důvěryhodné, aniž by byla ohrožena soukromí uživatele, což je v mnoha regionech zákonný požadavek.

## K čemu slouží

PCA existuje za účelem řešení konfliktu mezi bezpečností a soukromím v komunikaci [V2X](/mobilnisite/slovnik/v2x/). Zprávy V2X musí být autentizovány, aby se zabránilo podvržení a zajistila bezpečnost, ale použití pevné identity by umožnilo sledování vozidel, což by porušovalo soukromí řidiče. PCA tento problém řeší tím, že poskytuje vozidlům měnící se pseudonymy, což umožňuje autentizaci bez trvalého odhalení identity.

Historicky rané návrhy zabezpečení V2X používaly dlouhodobé certifikáty, které představovaly významná rizika pro soukromí. Koncept pseudonymních certifikátů byl vyvinut ve výzkumu a standardizován orgány jako IEEE 1609.2 a ETSI. 3GPP tento model přijala pro své specifikace Cellular V2X (C-V2X), aby vyhověla předpisům na ochranu soukromí (např. GDPR) a veřejným obavám. Řeší tak omezení jednodušších autentizačních schémat, která postrádala ochranu soukromí.

Integrace do standardů 3GPP zajišťuje, že mobilní sítě mohou podporovat škálovatelnou, spravovanou PKI pro miliony vozidel. To motivuje vytváření standardizovaných rozhraní a procedur pro PCA, což usnadňuje globální interoperabilitu pro bezpečné a na soukromí dbající systémy inteligentní dopravy.

## Klíčové vlastnosti

- Vydává krátkodobé pseudonymní certifikáty pro vozidla
- Umožňuje autentizaci bez odhalení dlouhodobé identity
- Integruje se s hierarchickou PKI pro V2X (Root CA, LTCA)
- Podporuje hromadné poskytování certifikátů pro offline použití
- Zajišťuje soulad s předpisy na ochranu soukromí (např. GDPR)
- Spolupracuje s řídicími funkcemi V2X podle 3GPP pro autorizaci

## Související pojmy

- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 33.885** (Rel-14) — Security Study for V2X Services

---

📖 **Anglický originál a plná specifikace:** [PCA na 3GPP Explorer](https://3gpp-explorer.com/glossary/pca/)
