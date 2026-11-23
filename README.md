# Markethub API

Backend de un marketplace: usuarios, catálogo, carrito, órdenes con control de stock, pagos simulados y reseñas.

![Estado](https://img.shields.io/badge/estado-en%20desarrollo-orange)
![Licencia](https://img.shields.io/badge/licencia-MIT-green)
![CI](https://github.com/valensantarone/markethub-api/actions/workflows/ci.yml/badge.svg)

> 🚧 **Proyecto en desarrollo.** Lo estoy construyendo por versiones, planificado con GitHub Projects, issues y pull requests. Podés seguir el avance en la pestaña [Projects](../../projects) y [Issues](../../issues).

## ¿De qué se trata?

Es una API REST que simula el núcleo de un e-commerce tipo marketplace, con compradores, vendedores y administradores. Lo desarrollo para practicar y demostrar fundamentos de backend: autenticación, modelado de datos, concurrencia, testing, CI y despliegue.

## Funcionalidades previstas

- **Usuarios y autenticación:** registro, login con JWT (acceso y refresh) y roles (comprador, vendedor, admin).
- **Catálogo:** categorías y productos, con paginación, filtros y orden.
- **Carrito y órdenes:** órdenes con estados (pendiente, pagada, enviada, entregada, cancelada).
- **Stock con concurrencia:** dos compradores no pueden llevarse la última unidad; checkout idempotente.
- **Pagos simulados:** endpoint de pago y webhook con verificación de firma.
- **Reseñas y reputación** de vendedores.
- **Producción:** cache, rate limiting, tareas en segundo plano, logs estructurados y health check.

## Stack

| Área | Tecnología |
|---|---|
| Lenguaje y framework | Python 3.12 · FastAPI |
| Base de datos | PostgreSQL · SQLAlchemy · Alembic |
| Testing | pytest |
| Infraestructura | Docker · Docker Compose · GitHub Actions |

## Roadmap

| Versión | Contenido | Estado |
|---|---|---|
| v0.1 | Configuración, usuarios, autenticación y catálogo | ⏳ Pendiente |
| v0.2 | Carrito, órdenes y stock con concurrencia | ⏳ Pendiente |
| v0.3 | Pagos, reseñas, cache, rate limiting y tareas asíncronas | ⏳ Pendiente |
| v1.0 | Documentación, deploy y pulido final | ⏳ Pendiente |

## Estructura del repositorio

```text
app/        código de la API (routers, servicios, repositorios, modelos)
tests/      tests unitarios y de integración
docs/       arquitectura, modelo de datos y decisiones técnicas (ADRs)
.github/    plantillas de issues y PRs, workflows de CI
```

## Cómo correrlo

Próximamente (v0.1).

## Cómo trabajo en este repo

- Cada cambio nace de un **issue** y se integra con un **pull request**.
- Commits siguiendo [Conventional Commits](https://www.conventionalcommits.org/es/).
- Versionado semántico y releases con changelog.

## Autor

**Valentino Santarone** · Estudiante de Ingeniería en Sistemas de Información (UTN FRBA) y Técnico en Informática
[LinkedIn](https://www.linkedin.com/in/valentinosantarone) · [GitHub](https://github.com/valensantarone)

## Licencia

MIT. Ver el archivo [LICENSE](LICENSE).