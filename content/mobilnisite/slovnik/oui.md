---
slug: "oui"
url: "/mobilnisite/slovnik/oui/"
type: "slovnik"
title: "OUI – Organizational Unique Identifier"
date: 2025-01-01
abbr: "OUI"
fullName: "Organizational Unique Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/oui/"
summary: "Globálně jedinečný identifikátor přidělený organizaci autoritou IEEE Registration Authority. V 3GPP se používá v kontextu Edge Computing k identifikaci aplikačních klientů a serverů, což umožňuje zjiš"
---

OUI je globálně jedinečný identifikátor přidělený institutem IEEE a používaný v 3GPP Edge Computing k identifikaci aplikačních klientů a serverů pro zjišťování služeb a zabezpečenou komunikaci.

## Popis

Organizational Unique Identifier (OUI) je 24bitové číslo jedinečně přidělené organizaci autoritou [IEEE](/mobilnisite/slovnik/ieee/) Registration Authority. Tvoří první polovinu 48bitové [MAC](/mobilnisite/slovnik/mac/) adresy. V rámci ekosystému 3GPP, konkrétně pro Edge Computing ([EC](/mobilnisite/slovnik/ec/)) definovaný od verze 12, je OUI využíván nad svou tradiční síťovou roli. Slouží jako základní stavební prvek pro vytváření globálně jedinečných identifikátorů pro aplikační klienty ([AC](/mobilnisite/slovnik/ac/)) a aplikační servery ([AS](/mobilnisite/slovnik/as/)) fungující v rámci architektury služeb Edge Computing. Tyto identifikátory jsou klíčové pro procedury zjišťování služeb, které umožňují AC nalézt odpovídající AS poskytující požadovanou edge aplikaci. Dále je identifikátor založený na OUI používán v bezpečnostních kontextech, například v rámci certifikátu TLS pro službu EC, k autentizaci AS. Integrace OUI do standardů 3GPP poskytuje stabilní, dobře známý a globálně spravovaný jmenný prostor, který zabraňuje kolizím identifikátorů mezi různými výrobci a poskytovateli služeb v distribuovaném edge prostředí. Jeho použití je specifikováno v procedurách pro Edge Configuration a Service Discovery.

## K čemu slouží

OUI bylo začleněno do standardů 3GPP, aby vyřešilo základní problém jedinečné identifikace entit v decentralizovaném, vícevýrobcovém prostředí Edge Computing. Před jeho přijetím 3GPP postrádalo standardizovaný, globálně jedinečný mechanismus pro identifikaci entit na aplikační úrovni mimo tradiční identifikátory účastníků a síťových prvků jádra sítě. Motivace vycházela z potřeby Edge Computing, kde musí být aplikační servery různých poskytovatelů zjistitelné a adresovatelné uživatelským zařízením důvěryhodným způsobem. Použití již existujícího schématu [IEEE](/mobilnisite/slovnik/ieee/) OUI poskytlo okamžité, robustní řešení bez nutnosti vytvářet nový, složitý správní orgán. Řeší omezení ad-hoc nebo lokálně omezených pojmenovacích systémů tím, že zajišťuje globální jedinečnost, což je zásadní pro zabezpečení (prevence podvržení) a pro škálovatelné zjišťování služeb napříč administrativními a národními hranicemi.

## Klíčové vlastnosti

- Globálně jedinečný 24bitový identifikátor spravovaný institutem IEEE
- Tvoří základ pro konstrukci identifikátorů pro edge aplikační klienty a servery
- Umožňuje standardizované procedury zjišťování služeb v 3GPP Edge Computing
- Používá se v bezpečnostních mechanismech, jako je identifikace v certifikátu TLS pro edge služby
- Zabraňuje kolizím v jmenném prostoru mezi různými výrobci zařízení a poskytovateli služeb
- Poskytuje stabilní a dobře zavedený základ pro decentralizovanou správu identit

## Definující specifikace

- **TS 23.852** (Rel-12) — Study on GTP-based S2a for WLAN Access
- **TS 24.535** (Rel-19) — TS 24535: (g)PTP Message Delivery Protocol

---

📖 **Anglický originál a plná specifikace:** [OUI na 3GPP Explorer](https://3gpp-explorer.com/glossary/oui/)
