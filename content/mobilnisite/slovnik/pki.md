---
slug: "pki"
url: "/mobilnisite/slovnik/pki/"
type: "slovnik"
title: "PKI – Public Key Infrastructure"
date: 2025-01-01
abbr: "PKI"
fullName: "Public Key Infrastructure"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/pki/"
summary: "PKI je rámec politik, rolí, hardwaru, softwaru a procedur pro vytváření, správu, distribuci, používání, ukládání a odvolávání digitálních certifikátů. V 3GPP navazuje důvěru pro síťové entity, aplikac"
---

PKI je rámec pro vytváření, správu a používání digitálních certifikátů za účelem navázání důvěry a umožnění bezpečného ověřování, šifrování a podepisování pro síťové entity a uživatele v systémech 3GPP.

## Popis

Infrastruktura veřejného klíče (PKI) je komplexní systém, který umožňuje bezpečný elektronický přenos informací tím, že poskytuje důvěryhodný základ pro vydávání, správu a ověřování digitálních certifikátů, které vážou veřejné klíče k identitám. V architektuře 3GPP není PKI jediným síťovým prvkem, ale všudypřítomným rámcem, který podmiňuje důvěru pro širokou škálu služeb a síťových funkcí. Její klíčové součásti zahrnují certifikační autoritu ([CA](/mobilnisite/slovnik/ca/)), která vydává a podepisuje certifikáty; registrační autoritu ([RA](/mobilnisite/slovnik/ra/)), která ověřuje identitu před vydáním certifikátu; a validační autoritu nebo úložiště, které uchovává certifikáty a seznamy odvolaných certifikátů ([CRL](/mobilnisite/slovnik/crl/)).

Jak PKI funguje v kontextu 3GPP, zahrnuje několik procesů. Nejprve síťová entita (jako gNB, [MME](/mobilnisite/slovnik/mme/) nebo aplikační server) vygeneruje pár veřejného a privátního klíče. Poté vytvoří žádost o podepsání certifikátu ([CSR](/mobilnisite/slovnik/csr/)) důvěryhodné CA v rámci PKI operátora nebo třetí strany. CA po ověření identity entity prostřednictvím RA vydá digitální certifikát – digitálně podepsaný dokument, který uvádí, že obsažený veřejný klíč patří této konkrétní entitě. Tento certifikát je pak používán v bezpečnostních protokolech. Například v [TLS](/mobilnisite/slovnik/tls/) pro zabezpečení rozhraní N server předloží svůj certifikát klientovi k ověření své identity. Klient certifikát ověří kontrolou podpisu CA a stavu odvolání prostřednictvím CRL nebo [OCSP](/mobilnisite/slovnik/ocsp/).

Role PKI v síti je zásadní. Umožňuje vzájemné ověřování mezi síťovými funkcemi v architekturách založených na službách ([SBA](/mobilnisite/slovnik/sba/)), zabezpečuje poskytování přihlašovacích údajů pro UE a UICC, podporuje zákonné odposlechy tím, že poskytuje klíče pro šifrování, a ověřuje uživatele a zařízení pro aplikační služby. Je kotvou důvěry pro technologie jako síťové segmenty (slicing) v 5G, kde různé segmenty mohou vyžadovat odlišné bezpečnostní politiky a certifikáty. PKI zajišťuje, že každá entita v komplexním ekosystému 3GPP může být kryptograficky identifikována a důvěryhodná.

## K čemu slouží

PKI byla vytvořena k řešení základního problému škálovatelné důvěry v digitální komunikaci. Před PKI vyžadovala bezpečná komunikace předem sdílená tajemství mezi každou dvojicí entit, což je v rozsáhlých otevřených sítích, jako je internet nebo globální mobilní systémy, neproveditelné. Účelem PKI je poskytnout mechanismus, kdy dvě strany, které spolu předtím neměly žádný vztah, mohou navázat důvěru prostřednictvím řetězce certifikátů vedoucího zpět k vzájemně důvěryhodné třetí straně (CA).

V historickém kontextu 3GPP potřeba PKI rostla s každou generací. Raný GSM spoléhal na symetrické klíče v SIM kartě. S příchodem 3G a zavedením služeb založených na IP vznikla potřeba zabezpečeného webového přístupu, VPN a zabezpečení aplikací, což vyžadovalo digitální certifikáty. 3GPP standardizovalo PKI pro podporu funkcí, jako je architektura generického inicializačního procesu (GBA), kde UE získává od sítě aplikačně specifické klíče, což je proces zabezpečený PKI. Řeší také omezení ruční distribuce klíčů automatizací správy životního cyklu digitálních identit prostřednictvím vydávání, obnovování a odvolávání. Motivací bylo vytvořit flexibilní, standardy založený model důvěry, který by mohl podporovat vyvíjející se bezpečnostní požadavky mobilních sítí, od ověřování zařízení až po zabezpečení síťových segmentů a edge computingu v 5G a dalších generacích.

## Klíčové vlastnosti

- Vydává a spravuje digitální certifikáty X.509, které vážou klíče k identitám
- Poskytuje důvěryhodnou hierarchii certifikačních autorit (CA)
- Spravuje životní cyklus certifikátu: vydání, obnovení, pozastavení a odvolání
- Podporuje seznamy odvolaných certifikátů (CRL) a Online Certificate Status Protocol (OCSP)
- Umožňuje bezpečné vzájemné ověřování mezi síťovými funkcemi a entitami
- Tvoří základ důvěry pro TLS/SSL, digitální podpisy a zabezpečené poskytování přihlašovacích údajů

## Definující specifikace

- **TS 22.112** (Rel-8) — USAT Gateway System Specification
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 26.233** (Rel-15) — 3GPP Packet-Switched Streaming Service (PSS)
- **TS 29.116** (Rel-19) — REST-based protocol for xMB reference point
- **TS 29.368** (Rel-19) — Tsp Reference Point Stage 3 Specification
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 33.122** (Rel-19) — Security Architecture for CAPIF
- **TS 33.220** (Rel-19) — Generic Authentication Architecture (GAA); Generic Bootstrapping Architecture (GBA)
- **TS 33.221** (Rel-19) — Subscriber Certificate Distribution via GBA
- **TS 33.310** (Rel-19) — 3GPP Authentication Framework for Network Nodes
- **TS 33.320** (Rel-19) — H(e)NB Subsystem Security Architecture
- **TS 33.749** (Rel-19) — Study on security aspects of edge computing enhancement
- **TS 33.812** (Rel-9) — M2M Remote Subscription Management Security
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [PKI na 3GPP Explorer](https://3gpp-explorer.com/glossary/pki/)
